from dungeonrun.entity import BaseEntity
from dungeonrun.prop import NumberProp, Prop


class BaseConsumable(BaseEntity):
    name = Prop("BASE CONSUMABLE")
    description = Prop("BASE CONSUMABLE")
    item_type = Prop("consumable")

    def __init__(self, player, other):
        self.player = player
        self.other = other

    def dialogue(self):
        pass

    def effect(self):
        pass

    def use(self):
        pass


class HealingPotion(BaseConsumable):
    name = Prop("BASE HEALING POTION")
    health_point = NumberProp(0)

    visible_prop = [
        {
            "Name": "name",
        },
        {
            "Description": "description",
        },
        {
            "Healing Effect": "health_point",
        },
    ]

    @property
    def description(self):
        return Prop(f"Restores {self.effect()} health point")

    def dialogue(self, amount):
        print(f"You drink the {self.name} for {amount} health point.")

    def effect(self):
        return self.health_point.get()

    def use(self):
        effect = self.effect()
        self.dialogue(effect)

        amount = self.player.health_point.add(effect)
        if self.player.health_point.is_overflow():
            self.player.health_point.fix_overflow()

        return amount


class LesserHealingPotion(HealingPotion):
    name = Prop("Lesser Healing Potion")
    health_point = NumberProp(20)

    drop_chance = NumberProp(0.8)

    def effect(self):
        return super().effect() + self.player.misc.get() * 2


class GreaterHealingPotion(HealingPotion):
    name = Prop("Greater Healing Potion")
    health_point = NumberProp(40)

    drop_chance = NumberProp(0.6)

    def effect(self):
        return super().effect() + self.player.misc.get() * 4
