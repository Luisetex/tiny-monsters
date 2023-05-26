from dataclasses import dataclass


@dataclass
class StatStage:
    """This dataclass should hold the value of the stage for the given stat and the name of the stat it holds value for.  Its stage attribute is able to increase or decrease but always up to -6 or 6."""

    name: str
    stage: int

    def __init__(self, name: str):
        self.name = name
        self.stage = 0

    def increase_value(self, value: int):
        """Increase the value of the given stat by the given value."""
        self.stage += value
        if self.stage > 6:
            self.stage = 6

    def decrease_value(self, value: int):
        """Decrease the value of the given stat by the given value."""
        self.stage -= value
        if self.stage < -6:
            self.stage = -6

    def __str__(self):
        return f"{self.name}: {self.stage}"

    def __repr__(self):
        return self.__str__()


@dataclass
class StatStages:
    """This dataclass should hold the values of the different StatsStage for the folowing stats: attack, defense, sp_attack, sp_defense, speed. Their maximum and minimum values are -6 and +6 respectively. It should also be able to increase or decrease each stat by a given value."""

    attack: StatStage = StatStage("Attack")
    defense: StatStage = StatStage("Defense")
    sp_attack: StatStage = StatStage("Sp. Attack")
    sp_defense: StatStage = StatStage("Sp. Defense")
    speed: StatStage = StatStage("Speed")

    def increase_stat(self, stat: str, value: int):
        """Increase the value of the given stat by the given value."""
        if stat == "attack":
            self.attack.increase_value(value)
        elif stat == "defense":
            self.defense.increase_value(value)
        elif stat == "sp_attack":
            self.sp_attack.increase_value(value)
        elif stat == "sp_defense":
            self.sp_defense.increase_value(value)
        elif stat == "speed":
            self.speed.increase_value(value)

    def decrease_stat(self, stat: str, value: int):
        """Decrease the value of the given stat by the given value."""
        if stat == "attack":
            self.attack.decrease_value(value)
        elif stat == "defense":
            self.defense.decrease_value(value)
        elif stat == "sp_attack":
            self.sp_attack.decrease_value(value)
        elif stat == "sp_defense":
            self.sp_defense.decrease_value(value)
        elif stat == "speed":
            self.speed.decrease_value(value)

    def __str__(self):
        return f"{self.attack}\n{self.defense}\n{self.sp_attack}\n{self.sp_defense}\n{self.speed}"

    def __repr__(self):
        return self.__str__()
