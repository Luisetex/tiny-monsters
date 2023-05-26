import json

from src.models.elemental_type import ElementalType


def get_name() -> str:
    """Asks for user input for the name of the type and returns it."""
    name = input("Enter the name of the type: ")
    return name


def get_modifier() -> tuple[str, float]:
    """Asks for user input for the modifiers of the type and returns it. The input will ask for w (weak), i (immune), s (strong) and n (neutral) modifiers."""
    type_name = input("Enter the modifier of the type: ")
    modifier_value = input("Enter the value of the modifier: w, i, s or n: ")
    if modifier_value == "w":
        value = 0.5
    elif modifier_value == "i":
        value = 0
    elif modifier_value == "s":
        value = 2
    else:
        value = 1
    return type_name, value


def get_modifiers() -> dict[str, float]:
    """Asks for user input for the modifiers of the type and returns it. The input will ask for w (weak), i (immune), s (strong) and n (neutral) modifiers."""
    modifiers: dict[str, float] = {}
    while True:
        modifier_name, value = get_modifier()
        modifiers[modifier_name] = value
        if input("Do you want to add another modifier? (y/n): ") == "n":
            break
    return modifiers


def create_gametype() -> ElementalType:
    """Asks for user input for the name type and the type modifiers and returns a GameType object."""
    name = get_name()
    modifiers = get_modifiers()
    return ElementalType(name, modifiers)


def create_gametypes():
    """Asks for an arbitrary number of gametypes and stores them as a json file."""
    gametypes: list[ElementalType] = []
    while True:
        gametype = create_gametype()
        gametypes.append(gametype)
        if input("Do you want to add another gametype? (y/n): ") == "n":
            break
    with open("data/gametypes.json", "w") as file:
        json.dump([gametype.__dict__ for gametype in gametypes], file, indent=2)


if __name__ == "__main__":
    create_gametypes()
