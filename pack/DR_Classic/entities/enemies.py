import random

from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax

from .utils import RandomizedNumber


class Enemy(BaseEntity):
    name = Prop("BASE ENEMY")

    health_point = PropWithMax(1, 1)
    attack = RandomizedNumber(0, 0)
    hit_chance = NumberProp(0)
    crit_chance = NumberProp(0)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(0, 1)

    encounter_chance = NumberProp(0)

    visible_prop = [
        {
            "Name": "name",
        },
        {
            "Health Point": "health_point",
            "Attack": "attack",
        },
        {
            "Hit Chance": "hit_chance",
            "Crit Chance": "crit_chance",
            "Evade Chance": "evade_chance",
        },
    ]

    def __init__(self):
        super().__init__()
        self.health_point = NumberProp(
            random.randint(
                self.health_point.get(), self.health_point.max_value.get()
            )
        )
        self.experience_drop = NumberProp(
            random.randint(
                self.experience_drop.get(),
                self.experience_drop.max_value.get(),
            )
        )


class BlueSlime(Enemy):
    name = Prop("Blue Slime")

    health_point = PropWithMax(10, 21)
    attack = RandomizedNumber(0, 1)
    hit_chance = NumberProp(0)
    crit_chance = NumberProp(0)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(1, 2)

    encounter_chance = NumberProp(0)


class Rat(Enemy):
    name = Prop("Rat")

    health_point = PropWithMax(10, 20)
    attack = RandomizedNumber(0, 2)
    hit_chance = NumberProp(0.70)
    crit_chance = NumberProp(0.03)
    evade_chance = NumberProp(0.03)
    experience_drop = RandomizedNumber(1, 2)

    encounter_chance = NumberProp(0.75)


class Spider(Enemy):
    name = Prop("Spider")

    health_point = PropWithMax(30, 40)
    attack = RandomizedNumber(4, 7)
    hit_chance = NumberProp(0.75)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(5, 9)

    encounter_chance = NumberProp(0.25)


class Goblin(Enemy):
    name = Prop("Goblin")

    health_point = PropWithMax(20, 30)
    attack = RandomizedNumber(4, 7)
    hit_chance = NumberProp(0.75)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(5, 9)

    encounter_chance = NumberProp(0.25)
