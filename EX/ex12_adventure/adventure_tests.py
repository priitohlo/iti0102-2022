import string

import pytest, random

from adventure import World, Adventurer, Monster


@pytest.fixture
def world() -> World:
    world = World('example')
    adv1 = Adventurer('adv1', 'Fighter', 25, 10)
    adv2 = Adventurer('adv2', 'Fighter', 40, 15)
    druid = Adventurer('druid', 'Druid', 50, 50)
    mon1 = Monster('mon1', 'zombie', 20)
    mon2 = Monster('mon2', 'zombie', 30)
    animal = Monster('animal', 'Animal', 25)
    world.add_adventurer(adv1)
    world.add_adventurer(adv2)
    world.add_adventurer(druid)
    world.add_monster(mon1)
    world.add_monster(mon2)
    world.add_monster(animal)

    return world


def test_necromancers_not_active(world):
    assert world.necromancers_active_status is False


def test_hero_in_world(world):
    assert 'adv1' in [a.name for a in world.adventurer_list]


def test_monster_in_world(world):
    assert 'mon1' in [a.name for a in world.monster_list]


def test_druids(world):
    world.add_adventurer_by_name('druid')
    world.add_monster_by_name('animal')
    world.go_adventure()
    assert 'animal' not in [m.name for m in world.get_graveyard()]
    assert 'animal' in [m.name for m in world.get_monster_list()]


def test_adventurers_of_class_type_added(world):
    world.add_all_adventurers_of_class_type('Fighter')
    assert ['Fighter', 'Fighter'] == [a.class_type for a in world.get_active_adventurers()]


def test_monster_defeated_non_deadly(world):
    world.go_adventure(False)
    assert 'mon1' in [m.name for m in world.get_monster_list()]


def test_monster_defeated_deadly(world):
    world.add_monster_by_name('mon1')
    world.add_adventurer_by_name('adv1')
    world.go_adventure(True)
    assert 'mon1' in [m.name for m in world.get_graveyard()]


def test_adventurer_defeated_deadly(world):
    world.add_monster_by_name('mon2')
    world.add_adventurer_by_name('adv1')
    world.go_adventure(True)
    assert 'adv1' in [a.name for a in world.get_graveyard()]


def test_hero_xp_gained_deadly(world):
    world.add_monster_by_name('mon1')
    world.add_adventurer_by_name('adv1')
    world.go_adventure(True)
    hero = [a for a in world.get_adventurer_list() if a.name == 'adv1'][0]
    assert hero.experience == 50


def test_hero_xp_gained_non_deadly(world):
    world.add_monster_by_name('mon1')
    world.add_adventurer_by_name('adv1')
    world.go_adventure(False)
    hero = [a for a in world.get_adventurer_list() if a.name == 'adv1'][0]
    assert hero.experience == 30


def test_adventurer_removed_by_name(world):
    world.remove_character('adv1')
    assert 'adv1' in [m.name for m in world.get_graveyard()]


def test_adventurer_removed_from_graveyard_by_name(world):
    world.remove_character('adv1')
    world.remove_character('adv1')
    assert 'adv1' not in [m.name for m in world.get_graveyard()]


def test_monster_revived(world):
    world.add_monster_by_name('mon1')
    world.add_adventurer_by_name('adv1')
    world.go_adventure(True)
    world.necromancers_active(True)
    world.revive_graveyard()
    assert 'Undead mon1' in [m.name for m in world.get_monster_list()]


def test_strongest_adventurer_added(world):
    world.add_strongest_adventurer('Fighter')
    assert 'adv2' in [a.name for a in world.get_active_adventurers()]


def test_weakest_adventurer_added(world):
    world.add_weakest_adventurer('Fighter')
    assert 'adv1' in [a.name for a in world.get_active_adventurers()]


def test_most_experienced_adventurer_added(world):
    world.add_most_experienced_adventurer('Fighter')
    assert 'adv2' in [a.name for a in world.get_active_adventurers()]


def test_least_experienced_adventurer_added(world):
    world.add_least_experienced_adventurer('Fighter')
    assert 'adv1' in [a.name for a in world.get_active_adventurers()]


def test_strongest_monster_added(world):
    world.add_strongest_monster()
    assert 'mon2' in [m.name for m in world.get_active_monsters()]


def test_weakest_monster_added(world):
    world.add_weakest_monster()
    assert 'mon1' in [m.name for m in world.get_active_monsters()]


def test_all_monsters_added(world):
    world.add_all_monsters()
    assert sorted(['animal', 'mon1', 'mon2']) == sorted([m.name for m in world.get_active_monsters()])
