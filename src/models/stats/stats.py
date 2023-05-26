from dataclasses import dataclass

from src.models.stats.stats_stages import StatStages


@dataclass
class Stats:
    """This dataclass should hold the values for the stats of a creature. The stats should be the same as in pokemon."""

    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
