"""Tests for the ROBOTRAITS archetype engine."""

import unittest

from software.robotraits.archetypes import (
    ARCHETYPE_CATALOG,
    create_default_registry,
)
from software.robotraits.profiles import (
    ArchetypeSelection,
    BehavioralProfile,
    ordered_archetypes,
    validate_profile,
)


class ArchetypeEngineTests(unittest.TestCase):
    def setUp(self):
        self.registry = create_default_registry()

    def test_catalog_contains_fifteen_archetypes(self):
        self.assertEqual(len(ARCHETYPE_CATALOG), 15)
        self.assertEqual(len(self.registry.archetypes()), 15)

    def test_all_archetypes_reference_registered_traits(self):
        for archetype in self.registry.archetypes():
            for trait_id in archetype.trait_ids:
                self.assertIsNotNone(self.registry.get_trait(trait_id))

    def test_profile_orders_by_priority(self):
        profile = BehavioralProfile(
            profile_id="profile.test",
            name="Research and Precision",
            selections=(
                ArchetypeSelection("analytical_researcher", 2),
                ArchetypeSelection("precision_guardian", 5),
                ArchetypeSelection("creative_innovator", 1),
            ),
        )

        result = ordered_archetypes(profile, self.registry)
        self.assertEqual(
            [item[0].archetype_id for item in result],
            [
                "precision_guardian",
                "analytical_researcher",
                "creative_innovator",
            ],
        )

    def test_unknown_archetype_is_rejected(self):
        profile = BehavioralProfile(
            profile_id="profile.invalid",
            name="Invalid Profile",
            selections=(ArchetypeSelection("does_not_exist"),),
        )

        with self.assertRaises(ValueError):
            validate_profile(profile, self.registry)

    def test_duplicate_archetypes_are_rejected(self):
        with self.assertRaises(ValueError):
            BehavioralProfile(
                profile_id="profile.duplicate",
                name="Duplicate Profile",
                selections=(
                    ArchetypeSelection("technical_engineer"),
                    ArchetypeSelection("technical_engineer", 2),
                ),
            )

    def test_negative_priority_is_rejected(self):
        with self.assertRaises(ValueError):
            ArchetypeSelection("technical_engineer", -1)

    def test_profile_does_not_enable_itself_by_priority(self):
        profile = BehavioralProfile(
            profile_id="profile.disabled",
            name="Disabled Profile",
            selections=(ArchetypeSelection("precision_guardian", 100),),
            enabled=False,
        )
        self.assertFalse(profile.enabled)


if __name__ == "__main__":
    unittest.main()
