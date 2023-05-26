from src.models.game_type import GameType
from src.models.stats import Stats, StatStages


class Creature:
    def __init__(self, name: str, level: int, stats: Stats):
        self.name = name
        self.level = level
        self.stats = stats
        self.stats_stages = StatStages()
