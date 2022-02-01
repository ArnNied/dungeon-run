import time

from dungeonrun.encounter import Encounter
from dungeonrun.utils import clear_stdout, rng
from pack.DR_Classic.core.exceptions import (
    EnemyDead,
    PlayerDead,
    PlayerEscape,
)
from pack.DR_Classic.entities.enemies import Enemy
from pack.DR_Classic.entities.player import Player


class BattleSequence(Encounter):
    def __init__(self, main_actor: Player, other: Enemy):
        super().__init__(main_actor, other)
        self.cycle = 0

    def display(self):
        print(f"===== Battle: Cycle {self.cycle} =====")
        print(self.other.stringify_prop())
        print()
        print(self.main_actor.stringify_prop())
        print("==============================")

    def before(self):
        print(f"You have encountered {self.other.name.get()}")

    def execute(self):
        try:
            while True:
                self.cycle += 1

                time.sleep(1.5)
                clear_stdout()
                self.display()
                if not self.main_actor.health_point.get() <= 0:
                    action = self.player_action()
                else:
                    raise PlayerDead

                if not self.other.health_point.get() <= 0:
                    if action != "parry":
                        self.enemy_action()
                else:
                    raise EnemyDead
        except EnemyDead:
            print(f"{self.other.name.get()} has been killed")
        except PlayerEscape:
            print("You have succesfully escaped")
            time.sleep(2)

    def player_action(self):
        repeat = True
        while repeat:
            clear_stdout()
            self.display()
            available_action = {
                "attack": "attack",
                "parry": "parry",
                "inventory": "inventory",
                "escape": "escape",
            }

            print(
                " :: ".join([action.title() for action in available_action])
            )

            player_action = input("> ").lower()
            print()
            if player_action in available_action:
                repeat = getattr(self, player_action)()
            else:
                print("Invalid action")
                time.sleep(1)

        return player_action

    def enemy_action(self):
        if rng(self.other.hit_chance.get()):
            if rng(self.main_actor.evade_chance.get()):
                print("Attack evaded!")
            else:
                damage = self.other.calculate_attack()
                if rng(self.other.crit_chance.get()):
                    damage *= 2
                    print("CRITICAL")
                player_receive = round(
                    damage * (1 - self.main_actor.damage_reduction.get())
                )

                self.main_actor.health_point.subtract(player_receive)

                print(f"You have suffered {player_receive} damage")
        else:
            print(f"{self.other.name.get()} missed!")

    def attack(self):
        if rng(self.main_actor.hit_chance.get()):
            if rng(self.other.evade_chance.get()):
                print(f"{self.other} evaded")
            else:
                damage = self.main_actor.calculate_attack()

                if rng(self.main_actor.crit_chance.get()):
                    damage *= 2
                    print("CRITICAL: ", end="")

                self.other.health_point.subtract(round(damage))

                print(f"You have dealt {damage} damage")
        else:
            print("Attack missed")

    def parry(self):
        if rng(self.main_actor.parry_chance.get()):
            damage = self.other.calculate_attack()

            if rng(self.other.crit_chance.get()):
                damage *= 2
                print("CRITICAL: ", end="")

            enemy_receive = round(damage * 0.9)
            player_receive = round(
                damage * 0.1 * (1 - self.main_actor.damage_reduction.get())
            )

            self.other.health_point.subtract(enemy_receive)
            self.main_actor.health_point.subtract(player_receive)

            print("Parry successful")
            print(f"You received {player_receive} damage")
            print(f"{self.other.name.get()} received {enemy_receive} damage")

        else:
            damage = self.other.calculate_attack()

            if rng(self.other.crit_chance.get()):
                damage *= 2
                print("CRITICAL: ", end="")

            player_receive = round(
                damage * (1 - self.main_actor.damage_reduction.get())
            )

            self.main_actor.health_point.subtract(player_receive)

            print("Parry failed")
            print(f"You suffered {player_receive} damage")

    def escape(self):
        if rng(1 - self.main_actor.health_point.current_percentage()):
            raise PlayerEscape
        else:
            print("Escape failed")

    def inventory(self):
        print("Inventory under construction")
