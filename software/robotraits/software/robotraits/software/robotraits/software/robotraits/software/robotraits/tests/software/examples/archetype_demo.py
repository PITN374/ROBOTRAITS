"""Demonstrate composition of ROBOTRAITS archetypes."""

from robotraits.archetypes import create_default_registry
from robotraits.profiles import (
    ArchetypeSelection,
    BehavioralProfile,
    ordered_archetypes,
)


def main() -> None:
    registry = create_default_registry()

    profile = BehavioralProfile(
        profile_id="profile.research-assistant",
        name="Research Assistant",
        selections=(
            ArchetypeSelection("analytical_researcher", priority=10),
            ArchetypeSelection("collaborative_mentor", priority=7),
            ArchetypeSelection("precision_guardian", priority=9),
        ),
        context="research and knowledge synthesis",
        version="0.1.0",
        provenance="illustrative demonstration",
    )

    print(f"Profile: {profile.name}")
    print(f"Context: {profile.context}")
    print(f"Version: {profile.version}")
    print("\nArchetypes, highest priority first:")

    for selection, archetype in ordered_archetypes(profile, registry):
        print(f"\n{selection.priority:g} — {archetype.name}")
        print(f"  Traits: {', '.join(archetype.trait_ids)}")
        print(f"  Functions: {', '.join(archetype.ai_functions)}")

    print("\nSafety boundary:")
    print("Priorities organize profile metadata only.")
    print("Independent safety controls remain authoritative.")


if __name__ == "__main__":
    main()
