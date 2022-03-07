import time

from app.DR_Classic.core.exceptions import EnemyDead, PlayerDead, PlayerEscape
from app.DR_Classic.entities.enemies import Enemy
from app.DR_Classic.entities.player import Player
from dungeonrun.process import Process
from dungeonrun.utils import clear_stdout, rng


class PlayerEvent:
    def level_up(self, player: Player):
        clear_stdout()

        print("Level up")
        player.level.add(1)

        # INCREASE HP
        print("Max HP increased by 10")
        print("HP refilled")
        player.health_point.max_value.add(10)
        player.health_point.update(player.health_point.max_value.get())

        # INCREASE EXP REQUIRED
        player.experience.subtract(player.experience.max_value.get())
        player.experience.max_value.add(10)

        if (
            player.strength.get() < player.strength.max_value.get()
            or player.agility.get() < player.agility.max_value.get()
            or player.misc.get() < player.misc.max_value.get()
        ):
            print("You received an attribute point")
            self.allocate_point(player)
        else:
            print("Max attribute reached!")

        time.sleep(1)

    def allocate_point(self, player: Player):
        while True:
            time.sleep(1)

            # clear_stdout()
            print(
                f"\nStrength: {player.strength}    Agility: {player.agility}    Misc: {player.misc}",
                end="\n\n",
            )

            attributes = ["strength", "agility", "misc"]
            allowed_action = []

            for attribute in attributes:
                attr = getattr(player, attribute)
                if attr.get() < attr.max_value.get():
                    allowed_action.append(attribute)

            print(" :: ".join([action.upper() for action in allowed_action]))
            player_choice = input("> ").lower()

            if player_choice in allowed_action:
                getattr(player, player_choice).add(1)
                break
            else:
                print("Invalid input")


class BattleSequence(Process):
    def __init__(self, main_actor: Player, other: Enemy):
        super().__init__(main_actor=main_actor, other=other)
        self.cycle = 0

    def display(self):
        print(f"===== Battle: Cycle {self.cycle} =====")
        print(self.other.stringify_prop())
        print()
        print(self.main_actor.stringify_prop())
        print("==============================")

    def before(self):
        print(f"You have encountered {self.other.name.get()}")

    def after(self):
        time.sleep(1)
        self.main_actor.experience.add(100)
        while (
            self.main_actor.experience.get()
            >= self.main_actor.experience.max_value.get()
        ):
            PlayerEvent().level_up(self.main_actor)

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

            return True
        except PlayerEscape:
            print("You have succesfully escaped")

    def player_action(self):
        repeat = True
        while repeat:
            clear_stdout()
            self.display()
            available_action = [
                "attack",
                "parry",
                "inventory",
                "escape",
            ]

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
                print(f"{self.other.name.get()} evaded")
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
        raise PlayerEscape
        if rng(1 - self.main_actor.health_point.current_percentage()):
            raise PlayerEscape
        else:
            print("Escape failed")

    def inventory(self):
        print("Inventory under construction")
