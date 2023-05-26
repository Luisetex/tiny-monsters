def generate_creature(
    id_: int,
    name: str,
    hp: int,
    attack: int,
    defense: int,
    sp_attack: int,
    sp_defense: int,
    speed: int,
):
    creature = {
        "id": id_,
        "name": name,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed,
        },
    }
    return creature


def get_positive_integer():
    """Ask for user input to generate a creature and print it."""
    value = int(input("Enter a positive integer: "))
    if value < 0:
        print("The value must be a positive integer.")
        raise ValueError
    return value


def get_string():
    """Ask for user input to generate a creature name with a maximum number of 20 characters."""
    value = input("Enter a string: ")
    if len(value) > 20:
        print("The value must be a string with a maximum number of 20 characters.")
        raise ValueError
    return value


def get_id():
    """Ask for user input to generate a creature and print it."""
    try:
        id_ = get_positive_integer()
    except ValueError:
        id_ = get_positive_integer()
    return id_


def get_name():
    """Ask for user input to generate a creature and print it."""
    try:
        name = get_string()
    except ValueError:
        name = get_string()
    return name


def get_hp():
    """Ask for user input to generate a creature and print it."""
    try:
        hp = get_positive_integer()
    except ValueError:
        hp = get_positive_integer()
    return hp


def get_attack():
    """Ask for user input to generate a creature and print it."""
    try:
        attack = get_positive_integer()
    except ValueError:
        attack = get_positive_integer()
    return attack


def get_defense():
    """Ask for user input to generate a creature and print it."""
    try:
        defense = get_positive_integer()
    except ValueError:
        defense = get_positive_integer()
    return defense


def get_sp_attack():
    """Ask for user input to generate a creature and print it."""
    try:
        sp_attack = get_positive_integer()
    except ValueError:
        sp_attack = get_positive_integer()
    return sp_attack


def get_sp_defense():
    """Ask for user input to generate a creature and print it."""
    try:
        sp_defense = get_positive_integer()
    except ValueError:
        sp_defense = get_positive_integer()
    return sp_defense


def get_speed():
    """Ask for user input to generate a creature and print it."""
    try:
        speed = get_positive_integer()
    except ValueError:
        speed = get_positive_integer()
    return speed


def main():
    """Generate a creature and print it."""
    print("Enter id.")
    id_ = get_id()
    print("Enter name.")
    name = get_name()
    print("Enter hp.")
    hp = get_hp()
    print("Enter attack.")
    attack = get_attack()
    print("Enter defense.")
    defense = get_defense()
    print("Enter sp_attack.")
    sp_attack = get_sp_attack()
    print("Enter sp_defense.")
    sp_defense = get_sp_defense()
    print("Enter speed.")
    speed = get_speed()
    creature = generate_creature(id_, name, hp, attack, defense, sp_attack, sp_defense, speed)
    print(creature)


if __name__ == "__main__":
    main()
