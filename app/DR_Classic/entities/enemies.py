import random

from app.DR_Classic.entities.apparel import *
from app.DR_Classic.entities.consumables import (
    GreaterHealingPotion,
    LesserHealingPotion,
)
from app.DR_Classic.entities.weapons import *
from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax
from dungeonrun.utils import rng

from .utils import RandomizedNumber


class Enemy(BaseEntity):
    name = Prop("BASE ENEMY")

    health_point = RandomizedNumber(1, 1)
    attack = RandomizedNumber(0, 0)
    hit_chance = NumberProp(0)
    crit_chance = NumberProp(0)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(0, 1)

    process_chance = NumberProp(0)

    droptable = []

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
        hp = random.randint(
            self.health_point.get(), self.health_point.max_value.get()
        )

        self.health_point = PropWithMax(hp, hp)
        self.experience_drop = NumberProp(
            random.randint(
                self.experience_drop.get(),
                self.experience_drop.max_value.get(),
            )
        )

    def calculate_attack(self):
        return random.randint(self.attack.get(), self.attack.max_value.get())

    def drop_item(self):
        items = list(
            sorted(
                self.droptable, key=lambda x: getattr(x, "drop_chance").get()
            )
        )

        dropped_item = []
        for item in items:
            if rng(item.drop_chance.get()):
                dropped_item.append(item)

        return dropped_item


#######
# ??? #
#######
class BlueSlime(Enemy):
    name = Prop("Blue Slime")

    health_point = RandomizedNumber(10, 21)
    attack = RandomizedNumber(0, 1)
    hit_chance = NumberProp(0)
    crit_chance = NumberProp(0)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(1, 2)

    process_chance = NumberProp(0)

    droptable = [
        SwordThree,
        RappierThree,
        AxeThree,
        LightThree,
        HeavyThree,
    ]


########
# EASY #
########
class Rat(Enemy):
    name = Prop("Rat")

    health_point = RandomizedNumber(5, 12)
    attack = RandomizedNumber(0, 2)
    hit_chance = NumberProp(0.70)
    crit_chance = NumberProp(0.01)
    evade_chance = NumberProp(0.03)
    experience_drop = RandomizedNumber(10, 17)

    process_chance = NumberProp(0.6)

    droptable = [
        LesserHealingPotion,
        SwordOne,
    ]


class Spider(Enemy):
    name = Prop("Spider")

    health_point = RandomizedNumber(20, 30)
    attack = RandomizedNumber(7, 11)
    hit_chance = NumberProp(0.65)
    crit_chance = NumberProp(0.02)
    evade_chance = NumberProp(0.02)
    experience_drop = RandomizedNumber(15, 18)

    process_chance = NumberProp(0.4)

    droptable = [
        LesserHealingPotion,
        HeavyOne,
        RappierOne,
    ]


class Goblin(Enemy):
    name = Prop("Goblin")

    health_point = RandomizedNumber(30, 40)
    attack = RandomizedNumber(3, 7)
    hit_chance = NumberProp(0.7)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.05)
    experience_drop = RandomizedNumber(15, 18)

    process_chance = NumberProp(0.4)

    droptable = [
        LesserHealingPotion,
        LightOne,
        AxeOne,
    ]


##########
# MEDIUM #
##########
class Skeleton(Enemy):
    name = Prop("Skeleton")

    health_point = RandomizedNumber(40, 80)
    attack = RandomizedNumber(8, 12)
    hit_chance = NumberProp(0.7)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0.08)
    experience_drop = RandomizedNumber(27, 31)

    process_chance = NumberProp(0.65)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        HeavyOne,
        SwordTwo,
    ]


class GreenSlime(Enemy):
    name = Prop("Green Slime")

    health_point = RandomizedNumber(60, 80)
    attack = RandomizedNumber(12, 18)
    hit_chance = NumberProp(0.75)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0.06)
    experience_drop = RandomizedNumber(25, 35)

    process_chance = NumberProp(0.5)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        LightOne,
        AxeTwo,
    ]


class RedSlime(Enemy):
    name = Prop("Red Slime")

    health_point = RandomizedNumber(100, 130)
    attack = RandomizedNumber(4, 8)
    hit_chance = NumberProp(0.85)
    crit_chance = NumberProp(0.16)
    evade_chance = NumberProp(0.1)
    experience_drop = RandomizedNumber(25, 35)

    process_chance = NumberProp(0.5)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        HeavyOne,
        RappierTwo,
    ]


########
# HARD #
########
class Zombie(Enemy):
    name = Prop("Zombie")

    health_point = RandomizedNumber(100, 150)
    attack = RandomizedNumber(10, 17)
    hit_chance = NumberProp(0.6)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0)
    experience_drop = RandomizedNumber(38, 45)

    process_chance = NumberProp(0.6)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        AxeThree,
    ]


class HollowKnight(Enemy):
    name = Prop("Hollow Knight")

    health_point = RandomizedNumber(140, 200)
    attack = RandomizedNumber(18, 25)
    hit_chance = NumberProp(0.85)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.12)
    experience_drop = RandomizedNumber(40, 60)

    process_chance = NumberProp(0.4)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        HeavyTwo,
        SwordThree,
    ]


class FallenPaladin(Enemy):
    name = Prop("Fallen Paladin")

    health_point = RandomizedNumber(200, 250)
    attack = RandomizedNumber(10, 16)
    hit_chance = NumberProp(0.8)
    crit_chance = NumberProp(0.22)
    evade_chance = NumberProp(0.15)
    experience_drop = RandomizedNumber(40, 60)

    process_chance = NumberProp(0.4)

    droptable = [
        LesserHealingPotion,
        GreaterHealingPotion,
        LightTwo,
        RappierThree,
    ]


#############
# MINI BOSS #
#############
class Minotaur(Enemy):
    name = Prop("Minotaur")

    health_point = RandomizedNumber(350, 450)
    attack = RandomizedNumber(14, 20)
    hit_chance = NumberProp(0.95)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.05)
    experience_drop = RandomizedNumber(75, 95)

    process_chance = NumberProp(1)


class StoneGargoyle(Enemy):
    name = Prop("Stone Gargoyle")

    health_point = RandomizedNumber(500, 650)
    attack = RandomizedNumber(18, 26)
    hit_chance = NumberProp(0.95)
    crit_chance = NumberProp(0.12)
    evade_chance = NumberProp(0.15)
    experience_drop = RandomizedNumber(110, 130)

    process_chance = NumberProp(1)


########
# BOSS #
########
class Boss(Enemy):
    name = Prop("? ? ? ?")

    health_point = RandomizedNumber(700, 900)
    attack = RandomizedNumber(25, 35)
    hit_chance = NumberProp(0.95)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.1)
    experience_drop = RandomizedNumber(150, 200)

    process_chance = NumberProp(1)
