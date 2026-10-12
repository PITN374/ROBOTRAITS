"""ROBOTRAITS: configurable behavioral and cognitive intelligence."""

from .models import (
    Archetype,
    SafetyConstraint,
    Trait,
    TraitCategory,
)
from .registry import TraitRegistry

__all__ = [
    "Archetype",
    "SafetyConstraint",
    "Trait",
    "TraitCategory",
    "TraitRegistry",
]

__version__ = "0.1.0"
