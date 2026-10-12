"""Trait and archetype registry for ROBOTRAITS."""

from __future__ import annotations

from .models import Archetype, Trait


class TraitRegistry:
    """In-memory registry for versioned traits and archetypes."""

    def __init__(self) -> None:
        self._traits: dict[str, Trait] = {}
        self._archetypes: dict[str, Archetype] = {}

    def register_trait(self, trait: Trait) -> None:
        """Register a trait without silently replacing an existing one."""
        if trait.trait_id in self._traits:
            raise ValueError(
                f"Trait already registered: {trait.trait_id}"
            )

        self._traits[trait.trait_id] = trait

    def register_archetype(self, archetype: Archetype) -> None:
        """Register an archetype after validating its trait references."""
        if archetype.archetype_id in self._archetypes:
            raise ValueError(
                f"Archetype already registered: "
                f"{archetype.archetype_id}"
            )

        missing = [
            trait_id
            for trait_id in archetype.trait_ids
            if trait_id not in self._traits
        ]

        if missing:
            raise ValueError(
                "Archetype references unknown traits: "
                + ", ".join(missing)
            )

        self._archetypes[archetype.archetype_id] = archetype

    def get_trait(self, trait_id: str) -> Trait:
        """Retrieve a trait by its stable identifier."""
        try:
            return self._traits[trait_id]
        except KeyError:
            raise KeyError(f"Unknown trait: {trait_id}") from None

    def get_archetype(self, archetype_id: str) -> Archetype:
        """Retrieve an archetype by its stable identifier."""
        try:
            return self._archetypes[archetype_id]
        except KeyError:
            raise KeyError(
                f"Unknown archetype: {archetype_id}"
            ) from None

    def traits(self) -> tuple[Trait, ...]:
        """Return registered traits in registration order."""
        return tuple(self._traits.values())

    def archetypes(self) -> tuple[Archetype, ...]:
        """Return registered archetypes in registration order."""
        return tuple(self._archetypes.values())

    def traits_for_archetype(
        self, archetype_id: str
    ) -> tuple[Trait, ...]:
        """Return the trait objects belonging to an archetype."""
        archetype = self.get_archetype(archetype_id)

        return tuple(
            self.get_trait(trait_id)
            for trait_id in archetype.trait_ids
        )
