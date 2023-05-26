from dataclasses import dataclass


@dataclass
class GameType:
    """Generic type class that has a name and the different types it is weak or strong against. These values should be represented by a integer multiplier"""

    name: str
    attack_modifiers: dict[str, float]
