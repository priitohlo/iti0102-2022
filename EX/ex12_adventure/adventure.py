"""docstring."""
import copy
import math


class World:
    """docstring."""

    def __init__(self, python_master: str):
        """docstring."""
        self.python_master = python_master
        self.graveyard = list()
        self.adventurer_list = list()
        self.active_adventurer_list = list()
        self.monster_list = list()
        self.necromancers_active_status = False

    def necromancers_active(self, active: bool):
        self.necromancers_active_status = active

    def get_python_master(self):
        """docstring."""
        return self.python_master

    def get_graveyard(self):
        """docstring."""
        return self.graveyard

    def revive_graveyard(self):
        if self.necromancers_active_status:
            for c in self.graveyard:
                if type(c) == Adventurer:
                    self.monster_list.append(Monster(f'Undead {c.name}', f'Zombie {c.class_type}', c.power))
                elif type(c) == Monster:
                    c.type = 'Zombie'
                    self.monster_list.append(c)
            self.necromancers_active(False)
            self.graveyard.clear()

    def get_adventurer_list(self):
        """docstring."""
        return self.adventurer_list

    def get_active_adventurers(self):
        """docstring."""
        return sorted(self.active_adventurer_list, key=lambda x: x.experience, reverse=True)

    def get_monster_list(self):
        """docstring."""
        return self.monster_list

    def get_active_monsters(self):
        """docstring."""
        return self.monster_list

    def add_adventurer(self, character):
        """docstring."""
        self.adventurer_list.append(character) if type(character) == Adventurer else None

    def add_strongest_adventurer(self, class_type: str):
        self.active_adventurer_list.append(
            list(
                sorted([a for a in self.adventurer_list if a.class_type == class_type], key=lambda x: x.power,
                       reverse=True))[0])

    def add_weakest_adventurer(self, class_type: str):
        self.active_adventurer_list.append(
            list(
                sorted([a for a in self.adventurer_list if a.class_type == class_type], key=lambda x: x.power,
                       reverse=False))[0])

    def add_monster(self, character):
        """docstring."""
        self.monster_list.append(character) if type(character) == Monster else None


    def add_strongest_monster(self):
        """docstring."""
        pass

    def go_adventure(self, param):
        """docstring."""
        pass

    def remove_character(self, name):
        """docstring."""
        for character_list in [self.adventurer_list, self.monster_list]:
            if name in [c.name for c in character_list]:
                for i, c in enumerate(character_list):
                    if c.name == name:
                        self.graveyard.append(character_list.pop(i))
                        return

        if name in [c.name for c in self.graveyard]:
            for i, c in enumerate(self.graveyard):
                if c.name == name:
                    self.graveyard.pop(i)
                    return


class Adventurer():
    """docstring."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """docstring."""
        allowed_classes = ['Fighter', 'Druid', 'Wizard', 'Paladin']

        self.name = name
        self.class_type = class_type if class_type in allowed_classes else 'Fighter'
        self.power = power if power < 99 else 10
        self.experience = experience if experience >= 0 else 0

    def __repr__(self):
        """docstring."""
        return f'{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}.'

    def add_power(self, power: int):
        """docstring."""
        self.power += power

    def add_experience(self, experience: int):
        """docstring."""
        self.experience += experience if experience >= 0 else 0
        if self.experience > 99:
            self.add_power(math.floor(self.experience / 10))
            self.experience = 0


class Monster():
    """docstring."""

    def __init__(self, name: str, type: str, power: int):
        """docstring."""
        self.name = name
        self.power = power
        self.type = type

    def __repr__(self):
        """docstring."""
        return f'{self.name} of type {self.type}, Power: {self.power}.'

    @property
    def name(self):
        return f'Undead {self._name}' if self.type == 'Zombie' else self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
