"""Core data models for the ROBOTRAITS framework."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TraitCategory(str, Enum):
    COGNITIVE = "cognitive"
    ANALYTICAL = "analytical"
    CREATIVE = "creative"
    SOCIAL = "social"
    EMOTIONAL = "emotional"
    OPERATIONAL = "operational"
    TECHNICAL = "technical"
    ETHICAL = "ethical"
    PROTECTIVE = "protective"
    ADAPTIVE = "adaptive"
    COMMUNICATION = "communication"


@dataclass(frozen=True, slots=True)
class Trait:
    """A versioned behavioral or cognitive trait definition and value."""

    trait_id: str
    trait_name: str
    trait_category: TraitCategory
    definition: str

    measurement_method: str = "unspecified"
    value: float | None = None
    confidence: float | None = None

    context: dict[str, Any] = field(default_factory=dict)
    activation_conditions: tuple[str, ...] = ()
    behavioral_effects: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()

    version: str = "0.1.0"
    provenance: str = "unspecified"

    def __post_init__(self) -> None:
        for name in ("trait_id", "trait_name", "definition", "version"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")

        if self.value is not None:
            _validate_unit_interval(self.value, "value")

        if self.confidence is not None:
            _validate_unit_interval(self.confidence, "confidence")


@dataclass(frozen=True, slots=True)
class Archetype:
    """A configurable profile that combines multiple trait identifiers."""

    archetype_id: str
    name: str
    description: str

    trait_ids: tuple[str, ...] = ()
    ai_functions: tuple[str, ...] = ()
    application_domains: tuple[str, ...] = ()
    priorities: tuple[str, ...] = ()

    version: str = "0.1.0"
    provenance: str = "ROBOTRAITS specification"

    def __post_init__(self) -> None:
        for name in ("archetype_id", "name", "description", "version"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")

        if len(set(self.trait_ids)) != len(self.trait_ids):
            raise ValueError("trait_ids must not contain duplicates")


@dataclass(frozen=True, slots=True)
class SafetyConstraint:
    """A declared safety requirement, not a safety controller."""

    constraint_id: str
    description: str
    mandatory: bool = True
    enforcement_layer: str = "independent_safety_system"
    verification_method: str = "requires_engineering_validation"

    def __post_init__(self) -> None:
        for name in ("constraint_id", "description"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")


def _validate_unit_interval(value: float, field_name: str) -> None:
    """Require a finite numeric value between 0 and 1 inclusive."""
    import math

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a number")

    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{field_name} must be between 0 and 1")
