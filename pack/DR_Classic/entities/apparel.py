from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop


class Apparel(BaseEntity):
    name = Prop("BASE APPAREL")

    damage_reduction = NumberProp(0)
    parry_chance = NumberProp(0)

    visible_prop = [
        {
            "Name": "name",
        },
        {
            "Base Damage Reduction": "damage_reduction",
            "Base Parry Rate": "parry_chance",
        },
    ]

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name.get()}"

    def calculate_damage_reduction(self, player):
        return NumberProp(
            player.strength.get() * 4 / 100 + self.damage_reduction.get()
        )

    def calculate_parry_chance(self, player):
        return NumberProp(
            player.misc.get() * 7 / 100 + self.parry_chance.get()
        )

    # def drop_check(self):
    #     return rng(self.drop_chance.get())


# UNARMED
class Cloth(Apparel):
    name = Prop("Rugged Cloth")


# WEAPON TIERS
class TierOneApparel(Apparel):
    drop_chance = NumberProp(0.5)


class TierTwoApparel(Apparel):
    drop_chance = NumberProp(0.4)


class TierThreeApparel(Apparel):
    drop_chance = NumberProp(0.3)


###############
# Light Armor #
###############
class LightOne(TierOneApparel):
    name = Prop("Hide Armor")

    parry_rate = NumberProp(0.16)


class LightTwo(TierTwoApparel):
    name = Prop("Leather Armor")

    parry_rate = NumberProp(0.21)


class LightThree(TierThreeApparel):
    name = Prop("Studded Armor")

    parry_rate = NumberProp(0.26)


##############
# HeavyArmor #
##############
class HeavyOne(TierOneApparel):
    name = Prop("Chainmail Armor")

    damage_reduction = NumberProp(0.1)


class HeavyTwo(TierTwoApparel):
    name = Prop("Steel Armor")

    damage_reduction = NumberProp(0.15)


class HeavyThree(TierOneApparel):
    name = Prop("Daedric Armor")

    damage_reduction = NumberProp(0.2)
