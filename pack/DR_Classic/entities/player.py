import random

from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax

from .apparel import Cloth
from .weapons import Fist


class Player(BaseEntity):
    name = Prop("Player")

    strength = PropWithMax(0, 8)
    agility = PropWithMax(2, 8)
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
        },
    ]

    @property
    def attack(self):
        return self.weapon.get().calculate_attack(self)

    @property
    def hit_chance(self):
        return self.weapon.get().calculate_hit_chance(self)

    @property
    def crit_chance(self):
        return self.weapon.get().calculate_crit_chance(self)

    @property
    def damage_reduction(self):
        return self.apparel.get().calculate_damage_reduction(self)

    @property
    def parry_chance(self):
        return self.apparel.get().calculate_parry_chance(self)

    def calculate_attack(self):
        random.randint(self.attack.get(), self.attack.max_value.get())
