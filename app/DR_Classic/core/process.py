import time
from typing import Union

from app.DR_Classic.core.exceptions import EnemyDead, PlayerDead, PlayerEscape
from app.DR_Classic.entities.apparel import Apparel
from app.DR_Classic.entities.consumables import (
    GreaterHealingPotion,
    LesserHealingPotion,
)
from app.DR_Classic.entities.enemies import Enemy
from app.DR_Classic.entities.player import Player
from app.DR_Classic.entities.weapons import AxeThree, Weapon
from dungeonrun.process import Process
from dungeonrun.utils import clear_stdout, join_iter, rng


class BaseEvent:
    def __init__(self, player: Player):
        self.player = player


class LootEvent(BaseEvent):
    def handle_drop(self, item):
        getattr(self, f"{item.item_type.get()}_drop")(item)

    def equippable_drop(self, equippable: Union[Apparel, Weapon]):
        equippable = equippable()
        is_valid = False
        current_equipment = getattr(
            self.player, equippable.item_category.get()
        )

        while not is_valid:
            clear_stdout()
            print(
                "=========================================================="
            )
            print(f"You found a {equippable.name.get()}")
            print(equippable.stringify_prop())
            print()
            print(f"Your {current_equipment.get().name.get()}")
            print(current_equipment.get().stringify_prop())
            print(
                "=========================================================="
            )
            print("What do you want to do?\n")

            valid_action = ["take", "ignore"]
            print(join_iter(valid_action))
            user_input = input("> ").lower()

            if user_input in valid_action:
                is_valid = True
                if user_input == "take":
                    current_equipment.update(equippable)

                print(f"You {user_input} the {equippable.name.get()}.")
            else:
                print("Invalid action.")

            time.sleep(1)

    def consumable_drop(self, consumable):
        self.player.inventory.add(consumable)


class PlayerEvent(BaseEvent):
    def level_up(self):
        clear_stdout()

        print("Level up")
        self.player.level.add(1)

        # INCREASE HP
        print("Max HP increased by 10")
        print("HP refilled")
        self.player.health_point.max_value.add(10)
        self.player.health_point.update(
            self.player.health_point.max_value.get()
        )

        # INCREASE EXP REQUIRED
        self.player.experience.subtract(
            self.player.experience.max_value.get()
        )
        self.player.experience.max_value.add(10)

        if (
            self.player.strength.get() < self.player.strength.max_value.get()
            or self.player.agility.get() < self.player.agility.max_value.get()
            or self.player.misc.get() < self.player.misc.max_value.get()
        ):
            print("You received an attribute point")
            self.allocate_point()
        else:
            print("Max attribute reached!")

        time.sleep(1)

    def allocate_point(self):
        while True:
            time.sleep(1)

            print(
                f"\nStrength: {self.player.strength}    Agility: {self.player.agility}    Misc: {self.player.misc}\n",
            )

            attributes = ["strength", "agility", "misc"]
            valid_action = []

            for attribute in attributes:
                attr = getattr(self.player, attribute)
                if attr.get() < attr.max_value.get():
                    valid_action.append(attribute)

            print(join_iter(valid_action))
            player_choice = input("> ").lower()

            if player_choice in valid_action:
                getattr(self.player, player_choice).add(1)
                break
            else:
                print("Invalid attribute")


class BattleSequence(Process):
    def __init__(self, player: Player, other: Enemy):
        super().__init__(player=player, other=other)
        self.cycle = 0

    def display(self, clear=False):
        if clear:
            clear_stdout()

        print(f"===== Battle: Cycle {self.cycle} =====")
        print(self.other.stringify_prop())
        print()
        print(self.player.stringify_prop())
        print("==============================")

    def before(self):
        print(f"You have encountered {self.other.name.get()}")

    def after(self):
        time.sleep(1)

        exp_dropped = self.other.experience_drop.get()
        print(f"You received {exp_dropped} exp")
        time.sleep(1)
        self.player.experience.add(exp_dropped)
        while (
            self.player.experience.get()
            >= self.player.experience.max_value.get()
        ):
            PlayerEvent(self.player).level_up()

        dropped_item = self.other.drop_item()
        for item in dropped_item:
            clear_stdout()
            print(f"{self.other.name.get()} dropped a(n) {item.name.get()}")
            time.sleep(1)
            LootEvent(self.player).handle_drop(item)

        clear_stdout()

    def execute(self):
        self.before()
        result = self.main()

        time.sleep(2)

        if result:
            self.after()

        return result

    def main(self):
        try:
            while True:
                self.cycle += 1

                time.sleep(1.5)
                self.display(True)
                if not self.player.health_point.get() <= 0:
                    action = self.player_action()
                else:
                    raise PlayerDead

                if action == "inventory":
                    self.cycle -= 1
                    continue

                if not self.other.health_point.get() <= 0:
                    if action != "parry":
                        self.enemy_action()
                else:
                    raise EnemyDead
        except EnemyDead:
            print(f"{self.other.name.get()} has been killed")

            return True
        except PlayerEscape:
            print("You have succesfully escaped")

    def player_action(self):
        repeat = True
        while repeat:
            self.display(True)
            valid_action = [
                "attack",
                "parry",
                "inventory",
                "escape",
            ]

            print(join_iter(valid_action))
            player_action = input("> ").lower()

            print()

            if player_action in valid_action:
                repeat = getattr(self, player_action)()
            else:
                print("Invalid action")
                time.sleep(1)

        return player_action

    def enemy_action(self):
        if rng(self.other.hit_chance.get()):
            if rng(self.player.evade_chance.get()):
                print("Attack evaded!")
            else:
                damage = self.other.calculate_attack()
                if rng(self.other.crit_chance.get()):
                    damage *= 2
                    print("CRITICAL: ", end="")
                player_receive = round(
                    damage * (1 - self.player.damage_reduction.get())
                )

                self.player.health_point.subtract(player_receive)

                print(f"You have suffered {player_receive} damage")
        else:
            print(f"{self.other.name.get()} missed!")

    def attack(self):
        if rng(self.player.hit_chance.get()):
            if rng(self.other.evade_chance.get()):
                print(f"{self.other.name.get()} evaded!")
            else:
                damage = self.player.calculate_attack()

                if rng(self.player.crit_chance.get()):
                    damage *= 2
                    print("CRITICAL: ", end="")

                self.other.health_point.subtract(round(damage))

                print(f"You have dealt {damage} damage")
        else:
            print("Attack missed!")

    def parry(self):
        damage = self.other.calculate_attack()

        if rng(self.other.crit_chance.get()):
            damage *= 2
            print("CRITICAL: ", end="")

        if rng(self.player.parry_chance.get()):
            enemy_receive = round(damage * 0.9)
            player_receive = round(
                damage * 0.1 * (1 - self.player.damage_reduction.get())
            )

            self.other.health_point.subtract(enemy_receive)
            self.player.health_point.subtract(player_receive)

            print("Parry successful")
            print(f"You received {player_receive} damage")
            print(f"{self.other.name.get()} received {enemy_receive} damage")

        else:
            player_receive = round(
                damage * (1 - self.player.damage_reduction.get())
            )

            self.player.health_point.subtract(player_receive)

            print("Parry failed")
            print(f"You suffered {player_receive} damage")

    def escape(self):
        if rng(1 - self.player.health_point.current_percentage()):
            raise PlayerEscape
        else:
            print("Escape failed")

    def inventory(self):
        while True:
            time.sleep(1)
            self.display(True)

            self.player.inventory.display(self.player, self.other)

            valid_action = ["use", "return"]

            print(join_iter(valid_action))
            action, *item = input("> ").lower().split()

            if action in valid_action:
                if action == "return":
                    break

                self.player.inventory.use(
                    " ".join(item), self.player, self.other
                )

            else:
                print("Invalid action")
                time.sleep(1)
