import random
import time

from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop, PropWithMax
from dungeonrun.utils import convert_to_keys

from .apparel import Cloth, HeavyThree
from .weapons import Fist, SwordThree


class Inventory(BaseEntity):
    items = {}

    def add(self, new_item):
        converted_to_key = convert_to_keys(new_item.name.get())
        item = self.get(converted_to_key)

        if item:
            item["quantity"] += 1
        else:
            self.items[converted_to_key] = {
                "item": new_item,
                "quantity": 1,
            }

    def get(self, item_name):
        return self.items.get(convert_to_keys(item_name))

    def use(self, item_name, player, other):
        item = self.get(item_name)

        if item:
            item["item"](player, other).use()
            item["quantity"] -= 1
        else:
            print("Item not found.")
            return False

        self.clean_items()

        return True

    def clean_items(self):
        to_be_removed = []
        for index, (key, val) in enumerate(self.items.items()):
            if val["quantity"] <= 0:
                to_be_removed.append(key)

        for key in to_be_removed:
            self.items.pop(key)

    def display(self, player, other):
        output = []
        for item in self.items.values():
            initiated = item["item"](player, other)
            output.append(
                "\n".join(
                    [
                        f"Name: {initiated.name.get()}",
                        f"Description: {initiated.description.get()}",
                        f"QTY: {item['quantity']}",
                    ]
                )
            )

        print("\n\n".join(output) if output else "No available consumable(s)")


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

    inventory = Inventory()

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
        cap = 0.95

        return self._prop_limit(chance, cap)

    @property
    def crit_chance(self):
        chance = self.weapon.get().calculate_crit_chance(self)
        cap = 0.5

        return self._prop_limit(chance, cap)

    @property
    def damage_reduction(self):
        reduction = self.apparel.get().calculate_damage_reduction(self)
        cap = 0.75

        return self._prop_limit(reduction, cap)

    @property
    def parry_chance(self):
        chance = self.apparel.get().calculate_parry_chance(self)
        cap = 0.95

        return self._prop_limit(chance, cap)

    @property
    def evade_chance(self):
        chance = NumberProp(self.agility.get() * 3 / 100)
        cap = 1

        return self._prop_limit(chance, cap)

    def _prop_limit(self, value, cap):
        return value if value.get() <= cap else NumberProp(cap)

    def calculate_attack(self):
        return random.randint(self.attack.get(), self.attack.max_value.get())
