from src.models.elemental_type import ElementalType
from src.models.stats import Stats, StatStages


class Creature:
    def __init__(self, name: str, level: int, stats: Stats):
        self.name = name
        self.level = level
        self.stats = stats
        self.stats_stages = StatStages()
