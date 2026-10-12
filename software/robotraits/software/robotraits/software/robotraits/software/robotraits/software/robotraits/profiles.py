"""Composition of ROBOTRAITS archetypes into configurable profiles."""

from __future__ import annotations

from dataclasses import dataclass
import math

from .registry import TraitRegistry


@dataclass(frozen=True, slots=True)
class ArchetypeSelection:
    """One archetype and its relative profile priority."""

    archetype_id: str
    priority: float = 1.0

    def __post_init__(self) -> None:
        if not self.archetype_id.strip():
            raise ValueError("archetype_id must not be empty")
        if (isinstance(self.priority, bool)
                or not isinstance(self.priority, (int, float))
                or not math.isfinite(self.priority)
                or self.priority < 0):
            raise ValueError("priority must be a finite, non-negative number")


@dataclass(frozen=True, slots=True)
class BehavioralProfile:
    """A composition of archetypes for a specified use context."""

    profile_id: str
    name: str
    selections: tuple[ArchetypeSelection, ...]
    context: str = "general"
    version: str = "0.1.0"
    provenance: str = "user-configured"
    enabled: bool = True

    def __post_init__(self) -> None:
        for field_name in ("profile_id", "name", "context", "version"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} must not be empty")

        ids = [selection.archetype_id for selection in self.selections]
        if len(ids) != len(set(ids)):
            raise ValueError("An archetype may appear only once per profile")

        if not self.selections:
            raise ValueError("A profile must contain at least one archetype")


def validate_profile(
    profile: BehavioralProfile,
    registry: TraitRegistry,
) -> None:
    """Raise ValueError if any selected archetype is not registered."""
    for selection in profile.selections:
        try:
            registry.get_archetype(selection.archetype_id)
        except KeyError:
            raise ValueError(
                f"Unknown archetype: {selection.archetype_id}"
            ) from None


def ordered_archetypes(
    profile: BehavioralProfile,
    registry: TraitRegistry,
):
    """Return (selection, archetype) pairs, highest priority first.

    Ties preserve the order in which selections were supplied.
    This function only orders metadata; it does not choose or execute actions.
    """
    validate_profile(profile, registry)
    indexed = list(enumerate(profile.selections))
    indexed.sort(key=lambda pair: (-pair[1].priority, pair[0]))

    return tuple(
        (selection, registry.get_archetype(selection.archetype_id))
        for _, selection in indexed
    )
