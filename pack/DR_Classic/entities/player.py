import random

from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax

from .apparel import Cloth, HeavyThree
from .weapons import Fist, SwordThree

# class Inventory(BaseEntity):


class Player(BaseEntity):
    name = Prop("Player")

    strength = PropWithMax(0, 8)
    agility = PropWithMax(0, 8)
    misc = PropWithMax(0, 8)

    level = NumberProp(1)
    experience = PropWithMax(0, 20)

    health_point = PropWithMax(100, 100)

    weapon = Prop(Fist())
    apparel = Prop(Cloth())

    visible_prop = [
        {
            "Name": "name",
            "HP": "health_point",
        },
        {
            "Level": "level",
            "EXP": "experience",
        },
        {
            "Weapon": "weapon",
            "Apparel": "apparel",
        },
        {
            "Attack": "attack",
            "Hit Chance": "hit_chance",
            "Crit Chance": "crit_chance",
        },
        {
            "Damage Reduction": "damage_reduction",
            "Parry Chance": "parry_chance",
            "Evade Chance": "evade_chance",
        },
    ]

    @property
    def attack(self):
        return self.weapon.get().calculate_attack(self)

    @property
    def hit_chance(self):
        chance = self.weapon.get().calculate_hit_chance(self)
        cap = NumberProp(0.95)
        return chance if chance.get() <= cap.get() else cap

    @property
    def crit_chance(self):
        chance = self.weapon.get().calculate_crit_chance(self)
        cap = NumberProp(0.5)
        return chance if chance.get() <= cap.get() else cap

    @property
    def damage_reduction(self):
        reduction = self.apparel.get().calculate_damage_reduction(self)
        cap = NumberProp(0.75)
        return reduction if reduction.get() <= cap.get() else cap

    @property
    def parry_chance(self):
        chance = self.apparel.get().calculate_parry_chance(self)
        cap = NumberProp(0.95)
        return chance if chance.get() <= cap.get() else cap

    @property
    def evade_chance(self):
        chance = NumberProp(self.agility.get() * 3 / 100)
        cap = NumberProp(1)
        return chance if chance.get() <= cap.get() else cap

    def calculate_attack(self):
        return random.randint(self.attack.get(), self.attack.max_value.get())
