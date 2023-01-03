"""docstring."""
import math


class World:
    """docstring."""

    def __init__(self, python_master: str):
        """docstring."""
        self.powers = None
        self.adventurers_upgraded = False
        self.python_master = python_master
        self.graveyard = list()
        self.adventurer_list = list()
        self.active_adventurer_list = list()
        self.monster_list = list()
        self.active_monster_list = list()
        self.necromancers_active_status = False

    def necromancers_active(self, active: bool):
        """docstring."""
        self.necromancers_active_status = active

    def get_python_master(self):
        """docstring."""
        return self.python_master

    def get_graveyard(self):
        """docstring."""
        return self.graveyard

    def revive_graveyard(self):
        """docstring."""
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
        return list(sorted(self.active_adventurer_list, key=lambda x: x.experience, reverse=True))

    def get_monster_list(self):
        """docstring."""
        return self.monster_list

    def get_active_monsters(self):
        """docstring."""
        return list(sorted(self.active_monster_list, key=lambda x: x.power, reverse=True))

    def add_adventurer(self, character):
        """docstring."""
        self.adventurer_list.append(character) if type(character) == Adventurer else None

    def add_strongest_adventurer(self, class_type: str):
        """docstring."""
        self.add_adventurer_by_stat('power', True, class_type)

    def add_weakest_adventurer(self, class_type: str):
        """docstring."""
        self.add_adventurer_by_stat('power', False, class_type)

    def add_most_experienced_adventurer(self, class_type: str):
        """docstring."""
        self.add_adventurer_by_stat('experience', True, class_type)

    def add_least_experienced_adventurer(self, class_type: str):
        """docstring."""
        self.add_adventurer_by_stat('experience', False, class_type)

    def add_adventurer_by_stat(self, stat: str, hi_lo: bool, class_type: str):
        """docstring."""
        if class_type in [a.class_type for a in self.adventurer_list]:
            character_to_add = list(
                sorted([a for a in self.adventurer_list if
                        a.class_type == class_type], key=(lambda x, add_stat=stat: getattr(x, add_stat)),
                       reverse=hi_lo))[0]
            self.active_adventurer_list.append(character_to_add)
            self.adventurer_list.remove(character_to_add)

    def add_adventurer_by_name(self, name: str):
        """docstring."""
        for a in self.adventurer_list[:]:
            if a.name == name:
                self.active_adventurer_list.append(a)
                self.adventurer_list.remove(a)

    def add_all_adventurers_of_class_type(self, class_type: str):
        """docstring."""
        for a in self.adventurer_list[:]:
            if a.class_type == class_type:
                self.active_adventurer_list.append(a)
                self.adventurer_list.remove(a)

    def add_all_adventurers(self):
        """docstring."""
        self.active_adventurer_list += self.adventurer_list
        self.adventurer_list.clear()

    def add_monster(self, character):
        """docstring."""
        self.monster_list.append(character) if type(character) == Monster else None

    def add_monster_by_name(self, name: str):
        """docstring."""
        for a in self.monster_list[:]:
            if a.name == name:
                self.active_monster_list.append(a)
                self.monster_list.remove(a)

    def add_strongest_monster(self):
        """docstring."""
        if len(self.monster_list) > 0:
            strongest_monster = list(
                sorted(self.monster_list, key=lambda x: x.power, reverse=True))[0]
            self.active_monster_list.append(strongest_monster)
            self.monster_list.remove(strongest_monster)

    def add_weakest_monster(self):
        """docstring."""
        if len(self.monster_list) > 0:
            weakest_monster = list(
                sorted(self.monster_list, key=lambda x: x.power, reverse=False))[0]
            self.active_monster_list.append(weakest_monster)
            self.monster_list.remove(weakest_monster)

    def add_all_monsters_of_type(self, type: str):
        """docstring."""
        for m in self.monster_list[:]:
            if m.type == type:
                self.active_monster_list.append(m)
                self.monster_list.remove(m)

    def add_all_monsters(self):
        """docstring."""
        self.active_monster_list += self.monster_list
        self.monster_list.clear()

    def remove_character(self, name):
        """docstring."""
        for character_list in [self.adventurer_list, self.monster_list]:
            if name in [c.name for c in character_list]:
                for c in character_list:
                    if c.name == name:
                        self.graveyard.append(c)
                        character_list.remove(c)
                return

        if name in [c.name for c in self.graveyard]:
            for c in self.graveyard[:]:
                if c.name == name:
                    self.graveyard.remove(c)

    def go_adventure(self, deadly: bool = False):
        """docstring."""
        self.remove_active_monsters_by_character_effect()
        self.enhance_adventurers_by_monster_effect()
        self.powers = self.calculate_powers()

        if self.adventurers_upgraded:
            for a in [a for a in self.active_adventurer_list if a.class_type == 'Paladin']:
                a.power //= 2
            self.adventurers_upgraded = False

        if deadly:
            if self.powers['adventurers'] > self.powers['monsters']:
                self.calculate_experience(deadly=True)
                self.kill_characters('monster')
                self.deactivate_characters('adventurer')
            elif self.powers['adventurers'] < self.powers['monsters']:
                self.kill_characters('adventurer')
                self.deactivate_characters('monster')
            elif self.powers['adventurers'] == self.powers['monsters']:
                self.calculate_experience(tie=True)
        elif not deadly:
            if self.powers['adventurers'] > self.powers['monsters']:
                self.calculate_experience()
            elif self.powers['adventurers'] == self.powers['monsters']:
                self.calculate_experience(tie=True)
            self.deactivate_characters('adventurer')
            self.deactivate_characters('monster')

        self.powers = None

    def kill_characters(self, character_type: str):
        """docstring."""
        if character_type == 'adventurer':
            for a in self.active_adventurer_list:
                self.graveyard.append(a)
            self.active_adventurer_list.clear()
        elif character_type == 'monster':
            for m in self.active_monster_list:
                self.graveyard.append(m)
            self.active_monster_list.clear()

    def deactivate_characters(self, character_type: str):
        """docstring."""
        if character_type == 'adventurer':
            self.adventurer_list += self.active_adventurer_list
            self.active_adventurer_list.clear()
        elif character_type == 'monster':
            self.monster_list += self.active_monster_list
            self.active_monster_list.clear()

    def calculate_powers(self) -> dict:
        """docstring."""
        return {'adventurers': sum([a.power if a else 0 for a in self.active_adventurer_list]),
                'monsters': sum([m.power if m else 0 for m in self.active_monster_list])}

    def calculate_experience(self, tie: bool = False, deadly: bool = False):
        """docstring."""
        for a in self.active_adventurer_list:
            if tie:
                a.add_experience(math.floor(self.powers['monsters'] / len(self.active_adventurer_list) / 2))
            elif not tie and not deadly:
                a.add_experience(math.floor(self.powers['monsters'] / len(self.active_adventurer_list)))
            elif not tie and deadly:
                a.add_experience(math.floor(self.powers['monsters'] / len(self.active_adventurer_list) * 2))

    def remove_active_monsters_by_character_effect(self):
        """docstring."""
        if "Druid" in [a.class_type for a in self.active_adventurer_list]:
            for m in self.active_monster_list[:]:
                if m.type in ["Animal", "Ent"]:
                    self.monster_list.append(m)
                    self.active_monster_list.remove(m)

    def enhance_adventurers_by_monster_effect(self):
        """docstring."""
        check_monsters = ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin", "Zombie Wizard"]
        if (m for m in check_monsters if m in [m.type for m in self.active_monster_list]):
            for a in self.active_adventurer_list:
                if a.class_type == "Paladin":
                    a.power *= 2
            self.adventurers_upgraded = True


class Adventurer:
    """docstring."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """docstring."""
        allowed_classes = ['Fighter', 'Druid', 'Wizard', 'Paladin']

        self.name = name
        self.class_type = class_type if class_type in allowed_classes else 'Fighter'
        self.power = power if power <= 99 else 10
        self.experience = 0
        if experience > 0:
            self.add_experience(experience)

    def __repr__(self):
        """docstring."""
        return f'{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}.'

    def add_power(self, power: int):
        """docstring."""
        self.power += power

    def add_experience(self, experience: int):
        """docstring."""
        if experience <= 0:
            return
        self.experience += experience
        if self.experience > 99:
            self.add_power(int(self.experience / 10))
            self.experience = 0


class Monster:
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
        """docstring."""
        return f'Undead {self._name}' if self.type == 'Zombie' else self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == "__main__":
    adv1 = Adventurer('ndtaqfwbnfvgdzquqmvlctjrfduuxv', 'Paladin', 99, 10)
    print(adv1)
