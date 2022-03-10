from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop

from .utils import RandomizedNumber


class Weapon(BaseEntity):
    name = Prop("BASE WEAPON")
    item_type = Prop("equippable")
    item_category = Prop("weapon")

    attack = RandomizedNumber(1, 1)
    hit_chance = NumberProp(0)
    crit_chance = NumberProp(0)
    drop_chance = NumberProp(0)

    visible_prop = [
        {
            "Name": "name",
        },
        {
            "Base Attack": "attack",
            "Base Hit Chance": "hit_chance",
            "Base Crit Chance": "crit_chance",
        },
    ]

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name.get()}"

    def calculate_attack(self, player):
        return RandomizedNumber(
            player.strength.get() * 2 + self.attack.get(),
            player.strength.get() * 2 + self.attack.max_value.get(),
        )

    def calculate_hit_chance(self, player):
        return NumberProp(
            player.agility.get() * 2 / 100 + self.hit_chance.get(),
        )

    def calculate_crit_chance(self, player):
        return NumberProp(
            player.misc.get() * 2 / 100 + self.crit_chance.get(),
        )

    # def drop_check(self):
    #     return rng(self.drop_chance.get())


# UNARMED
class Fist(Weapon):
    name = Prop("Fist")

    attack = RandomizedNumber(2, 6)
    hit_chance = NumberProp(0.75)
    crit_chance = NumberProp(0.05)


# WEAPON TIERS
class TierOneWeapon:
    drop_chance = NumberProp(0.6)


class TierTwoWeapon:
    drop_chance = NumberProp(0.5)


class TierThreeWeapon:
    drop_chance = NumberProp(0.4)


##########
# SWORDS #
##########
class Sword(Weapon):
    def calculate_attack(self, player):
        return RandomizedNumber(
            player.strength.get() * 3 + self.attack.get(),
            player.strength.get() * 3 + self.attack.max_value.get(),
        )

    def calculate_hit_chance(self, player):
        return NumberProp(
            player.agility.get() * 3 / 100 + self.hit_chance.get(),
        )

    def calculate_crit_chance(self, player):
        return NumberProp(
            player.misc.get() * 2 / 100 + self.crit_chance.get(),
        )


class SwordOne(TierOneWeapon, Sword):
    name = Prop("Iron Sword")

    attack = RandomizedNumber(7, 13)
    hit_chance = NumberProp(0.32)
    crit_chance = NumberProp(0.04)


class SwordTwo(TierTwoWeapon, Sword):
    name = Prop("Steel Sword")

    attack = RandomizedNumber(14, 20)
    hit_chance = NumberProp(0.42)
    crit_chance = NumberProp(0.08)


class SwordThree(TierThreeWeapon, Sword):
    name = Prop("Daedric Sword")

    attack = RandomizedNumber(22, 29)
    hit_chance = NumberProp(0.52)
    crit_chance = NumberProp(0.12)


########
# Axes #
########
class Axe(Weapon):
    def calculate_attack(self, player):
        return RandomizedNumber(
            player.strength.get() * 4 + self.attack.get(),
            player.strength.get() * 4 + self.attack.max_value.get(),
        )

    def calculate_hit_chance(self, player):
        return NumberProp(
            player.agility.get() * 1 / 100 + self.hit_chance.get(),
        )

    def calculate_crit_chance(self, player):
        return NumberProp(
            player.misc.get() * 2 / 100 + self.crit_chance.get(),
        )


class AxeOne(Axe, TierOneWeapon):
    name = Prop("Iron Axe")

    attack = RandomizedNumber(12, 23)
    hit_chance = NumberProp(0.21)
    crit_chance = NumberProp(0.06)


class AxeTwo(Axe, TierTwoWeapon):
    name = Prop("Steel Axe")

    attack = RandomizedNumber(18, 39)
    hit_chance = NumberProp(0.26)
    crit_chance = NumberProp(0.08)


class AxeThree(Axe, TierThreeWeapon):
    name = Prop("Daedric Axe")

    attack = RandomizedNumber(24, 45)
    hit_chance = NumberProp(0.31)
    crit_chance = NumberProp(0.1)


############
# Rappiers #
############
class Rapier(Weapon):
    def calculate_attack(self, player):
        return RandomizedNumber(
            player.strength.get() * 2 + self.attack.get(),
            player.strength.get() * 2 + self.attack.max_value.get(),
        )

    def calculate_hit_chance(self, player):
        return NumberProp(
            player.agility.get() * 2 / 100 + self.hit_chance.get(),
        )

    def calculate_crit_chance(self, player):
        return NumberProp(
            player.misc.get() * 3 / 100 + self.crit_chance.get(),
        )


class RappierOne(Rapier, TierOneWeapon):
    name = Prop("Iron Rappier")

    attack = RandomizedNumber(7, 10)
    hit_chance = NumberProp(0.37)
    crit_chance = NumberProp(0.03)


class RappierTwo(Rapier, TierTwoWeapon):
    name = Prop("Steel Rappier")

    attack = RandomizedNumber(12, 15)
    hit_chance = NumberProp(0.5)
    crit_chance = NumberProp(0.09)


class RappierThree(Rapier, TierThreeWeapon):
    name = Prop("Daedric Rappier")

    attack = RandomizedNumber(17, 21)
    hit_chance = NumberProp(0.63)
    crit_chance = NumberProp(0.15)
