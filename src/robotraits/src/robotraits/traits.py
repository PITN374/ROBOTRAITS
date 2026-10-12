"""Canonical ROBOTRAITS registry of 100 robotic traits."""

from dataclasses import dataclass
from enum import StrEnum


class TraitCategory(StrEnum):
    PHYSICAL = "physical"
    COGNITIVE = "cognitive"
    SENSORY = "sensory"
    OPERATIONAL = "operational"
    TECHNICAL = "technical"
    SAFETY = "safety"
    SOCIAL = "social"
    ADAPTIVE = "adaptive"
    DIGITAL = "digital"


@dataclass(frozen=True, slots=True)
class TraitDefinition:
    trait_id: str
    name: str
    category: TraitCategory
    definition: str
    value_kind: str
    unit: str | None = None


TRAIT_NAMES = (
    "Dexterity", "Strength", "Precision", "Accuracy", "Speed",
    "Agility", "Mobility", "Stability", "Balance", "Coordination",
    "Flexibility", "Adaptability", "Responsiveness", "Sensitivity",
    "Perception", "Awareness", "Intelligence", "Autonomy", "Learning",
    "Reasoning", "Planning", "Decision-Making", "Problem-Solving",
    "Predictability", "Reliability", "Durability", "Robustness",
    "Resilience", "Efficiency", "Endurance", "Stamina", "Repeatability",
    "Controllability", "Maneuverability", "Articulation", "Compliance",
    "Rigidity", "Torque", "Force", "Payload", "Reach", "Range",
    "Resolution", "Tactility", "Haptics", "Proprioception", "Kinesthesia",
    "Localization", "Navigation", "Spatiality", "Manipulability",
    "Graspability", "Slip-Resistance", "Contact-Sensitivity",
    "Thermosensitivity", "Pressure-Sensitivity", "Vibration-Sensitivity",
    "Auditory", "Visual", "Multimodality", "Synchronization", "Latency",
    "Throughput", "Connectivity", "Interoperability", "Compatibility",
    "Modularity", "Scalability", "Maintainability", "Serviceability",
    "Repairability", "Upgradability", "Reconfigurability", "Self-Diagnosis",
    "Self-Monitoring", "Self-Correction", "Self-Calibration",
    "Fault-Tolerance", "Redundancy", "Safety", "Security", "Explainability",
    "Transparency", "Interpretability", "Verifiability", "Traceability",
    "Accountability", "Energy-Efficiency", "Thermoregulation",
    "Noise-Reduction", "Lightweightness", "Compactness", "Softness",
    "Compliance-Control", "Human-Likeness", "Anthropomorphism", "Ergonomics",
    "Empathy", "Sociability", "Trustworthiness",
)


def _category(name: str) -> TraitCategory:
    """Assign a broad initial category to a trait."""
    key = name.casefold()

    if key in {"strength", "torque", "force", "payload", "reach",
               "rigidity", "softness", "lightweightness", "compactness"}:
        return TraitCategory.PHYSICAL

    if key in {"perception", "awareness", "auditory", "visual",
               "tactility", "haptics", "proprioception", "kinesthesia",
               "thermosensitivity", "pressure-sensitivity",
               "vibration-sensitivity", "contact-sensitivity"}:
        return TraitCategory.SENSORY

    if key in {"intelligence", "learning", "reasoning", "planning",
               "decision-making", "problem-solving"}:
        return TraitCategory.COGNITIVE

    if key in {"safety", "security", "fault-tolerance", "redundancy"}:
        return TraitCategory.SAFETY

    if key in {"empathy", "sociability", "human-likeness",
               "anthropomorphism"}:
        return TraitCategory.SOCIAL

    if key in {"adaptability", "resilience", "self-correction",
               "self-calibration", "reconfigurability"}:
        return TraitCategory.ADAPTIVE

    if key in {"connectivity", "interoperability", "compatibility",
               "throughput", "latency", "synchronization"}:
        return TraitCategory.DIGITAL

    return TraitCategory.OPERATIONAL


def _value_kind(name: str) -> str:
    """Distinguish physical measurements from scores and verification."""
    if name in {"Torque"}:
        return "measurement"
    if name in {"Force"}:
        return "measurement"
    if name in {"Payload"}:
        return "measurement"
    if name in {"Reach", "Range"}:
        return "measurement"
    if name == "Latency":
        return "measurement"
    if name == "Throughput":
        return "measurement"
    if name in {"Safety", "Security", "Verifiability"}:
        return "verification"
    return "score"


TRAITS: dict[str, TraitDefinition] = {
    f"RT-{index:03d}": TraitDefinition(
        trait_id=f"RT-{index:03d}",
        name=name,
        category=_category(name),
        definition=(
            f"ROBOTRAITS trait describing {name.casefold()}; "
            "its operational meaning and assessment method must be "
            "specified for the applicable system and context."
        ),
        value_kind=_value_kind(name),
    )
    for index, name in enumerate(TRAIT_NAMES, start=1)
}


def get_trait(name: str) -> TraitDefinition:
    """Find a trait by its name or canonical identifier."""
    query = name.strip().casefold()

    for trait in TRAITS.values():
        if query in {
            trait.name.casefold(),
            trait.trait_id.casefold(),
            trait.name.casefold().replace("-", "_").replace(" ", "_"),
        }:
            return trait

    raise KeyError(f"Unknown ROBOTRAITS trait: {name}")


def list_traits() -> tuple[TraitDefinition, ...]:
    """Return all 100 trait definitions in canonical order."""
    return tuple(TRAITS.values())
