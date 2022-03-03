import random

from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax

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
    experience_drop = RandomizedNumber(1, 2)

    process_chance = NumberProp(0.6)


class Spider(Enemy):
    name = Prop("Spider")

    health_point = RandomizedNumber(20, 30)
    attack = RandomizedNumber(7, 11)
    hit_chance = NumberProp(0.65)
    crit_chance = NumberProp(0.02)
    evade_chance = NumberProp(0.02)
    experience_drop = RandomizedNumber(5, 8)

    process_chance = NumberProp(0.4)


class Goblin(Enemy):
    name = Prop("Goblin")

    health_point = RandomizedNumber(30, 40)
    attack = RandomizedNumber(3, 7)
    hit_chance = NumberProp(0.7)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.05)
    experience_drop = RandomizedNumber(5, 8)

    process_chance = NumberProp(0.4)


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
    experience_drop = RandomizedNumber(12, 16)

    process_chance = NumberProp(0.65)


class GreenSlime(Enemy):
    name = Prop("Green Slime")

    health_point = RandomizedNumber(60, 80)
    attack = RandomizedNumber(12, 18)
    hit_chance = NumberProp(0.75)
    crit_chance = NumberProp(0.05)
    evade_chance = NumberProp(0.06)
    experience_drop = RandomizedNumber(10, 20)

    process_chance = NumberProp(0.5)


class RedSlime(Enemy):
    name = Prop("Red Slime")

    health_point = RandomizedNumber(100, 130)
    attack = RandomizedNumber(4, 8)
    hit_chance = NumberProp(0.85)
    crit_chance = NumberProp(0.16)
    evade_chance = NumberProp(0.1)
    experience_drop = RandomizedNumber(10, 20)

    process_chance = NumberProp(0.5)


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
    experience_drop = RandomizedNumber(18, 25)

    process_chance = NumberProp(0.6)


class HollowKnight(Enemy):
    name = Prop("Hollow Knight")

    health_point = RandomizedNumber(140, 200)
    attack = RandomizedNumber(18, 25)
    hit_chance = NumberProp(0.85)
    crit_chance = NumberProp(0.08)
    evade_chance = NumberProp(0.12)
    experience_drop = RandomizedNumber(20, 40)

    process_chance = NumberProp(0.4)


class FallenPaladin(Enemy):
    name = Prop("Fallen Paladin")

    health_point = RandomizedNumber(200, 250)
    attack = RandomizedNumber(10, 16)
    hit_chance = NumberProp(0.8)
    crit_chance = NumberProp(0.22)
    evade_chance = NumberProp(0.15)
    experience_drop = RandomizedNumber(20, 40)

    process_chance = NumberProp(0.4)


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
    experience_drop = RandomizedNumber(50, 70)

    process_chance = NumberProp(1)


class StoneGargoyle(Enemy):
    name = Prop("Stone Gargoyle")

    health_point = RandomizedNumber(500, 650)
    attack = RandomizedNumber(18, 26)
    hit_chance = NumberProp(0.95)
    crit_chance = NumberProp(0.12)
    evade_chance = NumberProp(0.15)
    experience_drop = RandomizedNumber(80, 100)

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
    experience_drop = RandomizedNumber(100, 150)

    process_chance = NumberProp(1)
