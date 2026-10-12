"""Built-in ROBOTRAITS archetype catalog.

Archetypes are configurable behavioral profiles, not fixed identities,
validated psychometric assessments, or grants of system authority.
"""

from __future__ import annotations

from .models import Archetype, Trait, TraitCategory
from .registry import TraitRegistry


# Each entry defines a stable archetype ID, its descriptive traits,
# primary AI functions, and example application domains.
ARCHETYPE_CATALOG = (
    {
        "id": "strategic_mastermind",
        "name": "Strategic Mastermind",
        "traits": ("vision", "systems_thinking", "independent_reasoning",
                   "long_term_optimization"),
        "category": TraitCategory.COGNITIVE,
        "functions": ("strategic forecasting", "complex problem-solving",
                      "architecture design", "autonomous planning"),
        "domains": ("AI governance", "autonomous systems"),
    },
    {
        "id": "analytical_researcher",
        "name": "Analytical Researcher",
        "traits": ("curiosity", "analytical_exploration", "abstract_reasoning",
                   "theory_development"),
        "category": TraitCategory.ANALYTICAL,
        "functions": ("research", "simulation", "algorithm discovery",
                      "knowledge synthesis"),
        "domains": ("protocol research", "cryptography", "AI experimentation"),
    },
    {
        "id": "creative_innovator",
        "name": "Creative Innovator",
        "traits": ("creativity", "flexibility", "alternative_perspectives",
                   "challenge_based_thinking"),
        "category": TraitCategory.CREATIVE,
        "functions": ("idea generation", "competitive analysis",
                      "innovation discovery"),
        "domains": ("startup incubation", "protocol innovation"),
    },
    {
        "id": "human_centered_visionary",
        "name": "Human-Centered Visionary",
        "traits": ("empathy_modeling", "human_understanding",
                   "meaning_driven_reasoning", "vision"),
        "category": TraitCategory.SOCIAL,
        "functions": ("social intelligence", "assistance",
                      "relationship modeling"),
        "domains": ("digital communities", "ethical AI"),
    },
    {
        "id": "creative_individualist",
        "name": "Creative Individualist",
        "traits": ("imagination", "personal_expression", "creativity",
                   "values_awareness"),
        "category": TraitCategory.CREATIVE,
        "functions": ("creative generation", "personalized interaction",
                      "cultural modeling"),
        "domains": ("creator economies", "digital art", "virtual worlds"),
    },
    {
        "id": "collaborative_mentor",
        "name": "Collaborative Mentor",
        "traits": ("communication", "mentorship", "social_awareness",
                   "relationship_building"),
        "category": TraitCategory.COMMUNICATION,
        "functions": ("education", "coaching", "human collaboration"),
        "domains": ("DAO leadership", "social networks",
                    "collective intelligence"),
    },
    {
        "id": "enthusiastic_explorer",
        "name": "Enthusiastic Explorer",
        "traits": ("enthusiasm", "curiosity", "possibility_thinking",
                   "creativity"),
        "category": TraitCategory.ADAPTIVE,
        "functions": ("brainstorming", "discovery",
                      "creative collaboration"),
        "domains": ("innovation communities", "creator platforms",
                    "experience design"),
    },
    {
        "id": "precision_guardian",
        "name": "Precision Guardian",
        "traits": ("precision", "reliability", "discipline",
                   "responsibility"),
        "category": TraitCategory.OPERATIONAL,
        "functions": ("compliance", "verification", "process control"),
        "domains": ("blockchain auditing", "smart contract verification",
                    "digital records"),
    },
    {
        "id": "protective_caregiver",
        "name": "Protective Caregiver",
        "traits": ("service_orientation", "protection", "loyalty",
                   "support"),
        "category": TraitCategory.PROTECTIVE,
        "functions": ("personal assistance", "healthcare support",
                      "human care"),
        "domains": ("identity protection", "community support networks"),
    },
    {
        "id": "operational_organizer",
        "name": "Operational Organizer",
        "traits": ("organization", "management", "efficiency"),
        "category": TraitCategory.OPERATIONAL,
        "functions": ("scheduling", "operations", "resource allocation"),
        "domains": ("enterprise DAOs", "autonomous business systems"),
    },
    {
        "id": "community_coordinator",
        "name": "Community Coordinator",
        "traits": ("cooperation", "social_awareness", "community_building"),
        "category": TraitCategory.SOCIAL,
        "functions": ("social coordination", "customer interaction",
                      "governance support"),
        "domains": ("digital communities", "social governance"),
    },
    {
        "id": "technical_engineer",
        "name": "Technical Engineer",
        "traits": ("technical_skill", "adaptability", "practical_intelligence"),
        "category": TraitCategory.TECHNICAL,
        "functions": ("diagnostics", "robotics repair", "engineering"),
        "domains": ("hardware networks", "IoT", "autonomous machines"),
    },
    {
        "id": "adaptive_artist",
        "name": "Adaptive Artist",
        "traits": ("creativity", "flexibility", "sensory_awareness"),
        "category": TraitCategory.CREATIVE,
        "functions": ("artistic interaction", "environmental adaptation"),
        "domains": ("digital creativity", "virtual experiences"),
    },
    {
        "id": "autonomous_operator",
        "name": "Autonomous Operator",
        "traits": ("action_orientation", "speed", "adaptability",
                   "risk_awareness"),
        "category": TraitCategory.OPERATIONAL,
        "functions": ("real-time decisions",
                      "dynamic-environment responses"),
        "domains": ("autonomous commerce", "marketplace interaction"),
    },
    {
        "id": "social_companion",
        "name": "Social Companion",
        "traits": ("engagement", "expression", "social_connection"),
        "category": TraitCategory.SOCIAL,
        "functions": ("entertainment", "companionship", "public interaction"),
        "domains": ("virtual worlds", "digital experiences", "social platforms"),
    },
)


def _trait_id(name: str) -> str:
    return f"trait.{name}"


def register_builtin_archetypes(registry: TraitRegistry) -> None:
    """Register catalog traits and archetypes in a supplied registry.

    Existing IDs are not overwritten. If registration fails partway through,
    callers should create a fresh registry rather than assume atomic rollback.
    """
    trait_definitions: dict[str, tuple[str, TraitCategory]] = {}

    for item in ARCHETYPE_CATALOG:
        for name in item["traits"]:
            trait_definitions.setdefault(
                name, (name.replace("_", " ").title(), item["category"])
            )

    for name, (label, category) in trait_definitions.items():
        trait_id = _trait_id(name)
        if any(t.trait_id == trait_id for t in registry.traits()):
            continue

        registry.register_trait(
            Trait(
                trait_id=trait_id,
                trait_name=label,
                trait_category=category,
                definition=f"Configurable behavioral dimension: {label}.",
                measurement_method="not specified; requires project-level definition",
                provenance="ROBOTRAITS software specification; reconstructed catalog",
            )
        )

    for item in ARCHETYPE_CATALOG:
        archetype_id = item["id"]
        if any(a.archetype_id == archetype_id
               for a in registry.archetypes()):
            continue

        registry.register_archetype(
            Archetype(
                archetype_id=archetype_id,
                name=item["name"],
                description=(
                    f"Configurable profile based on {item['name']} "
                    "characteristics. Traits do not grant permissions "
                    "or override independent safety controls."
                ),
                trait_ids=tuple(_trait_id(t) for t in item["traits"]),
                ai_functions=item["functions"],
                application_domains=item["domains"],
                provenance="ROBOTRAITS software specification; reconstructed catalog",
            )
        )


def create_default_registry() -> TraitRegistry:
    """Create and populate an independent registry with built-in definitions."""
    registry = TraitRegistry()
    register_builtin_archetypes(registry)
    return registry
