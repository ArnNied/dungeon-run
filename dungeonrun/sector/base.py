from time import sleep

from dungeonrun.actor.base import BaseActor
from dungeonrun.mechanics.encounter import Encounter
from dungeonrun.utils import (
    convert_to_keys,
    convert_to_readable,
    import_from_pack,
    rng,
)


class BaseSector:
    """
    Class to inherit when creating an sector.

    Note that this class should be inherited first (leftmost) before any sector mixin used.

    paths: {"sector_key": "module.class"}
    """

    paths = None
    path_separator = " :: "

    next_sector = None

    def __init__(self, player):
        self.player = player
        super().__init__()

    def execute(self) -> "BaseSector":
        """Main function to call."""

        self.paths_check()
        while self.next_sector == None:
            self.display_available_path()
            self.set_next_sector()

        imported_sector = self.import_next_sector(self.next_sector)

        return imported_sector

    def paths_check(self) -> None:
        """
        Check if self.paths is a string pointing to a sector.
        OR if self.paths is None then it will be considered an 'ending'.
        """

        if self.paths is None:
            print("end")
        elif type(self.paths) is str:
            self.next_sector = self.paths

    def display_available_path(self) -> None:
        """Output available path(s) to the terminal."""

        paths = [convert_to_readable(path) for path in self.paths]
        paths = self.path_separator.join(paths)

        print(f"\n{paths}")

    def set_next_sector(self) -> None:
        """Set self.next_sector for importing and executing."""

        player_choice = input("> ")

        # Convert from human-readable (user input) to dictionary keys for self.paths use.
        chosen_path = convert_to_keys(player_choice)
        chosen_path = self.paths.get(chosen_path, False)

        if chosen_path == False:
            print(f"Path {player_choice} doesn't exist")
        else:
            self.next_sector = chosen_path

    def import_next_sector(self, next_sector: str) -> "BaseSector":
        """Import the class of next sector to instantiate in main.py."""

        return import_from_pack(f"sector.{next_sector}")


class Dialogue:
    """
    Class to inherit when a sector need to display dialogue(s).

    dialogue: [{"text": string, "before": int|float, "after": int|float},]
    """

    dialogue = []

    def __init__(self):
        """Print dialogue(s) with delay before and/or after."""

        if self.dialogue is not None:
            for line in self.dialogue:
                sleep(line.get("before", 0))
                print(line["text"])
                sleep(line.get("after", 1))

        super().__init__()


class MultipleHostileEncounter:
    """
    Class to inherit when a sector will have multiple enemy encounter.

    enemies: ["module.class",]
    """

    enemies = []

    def __init__(self):
        enemies = self.encounter_check(self.import_enemies())

        for enemy in enemies:
            enemy = enemy()
            print(f"encountered {enemy.name.value.get()}")
            Encounter(self.player, enemy)
            print()

        super().__init__()

    def import_enemies(self) -> list[BaseActor]:
        """Import enemy module from the list self.enemies."""

        imported_enemies = [
            import_from_pack(f"enemies.{enemy}") for enemy in self.enemies
        ]

        # return sorted enemy by encounter_chance from lowest
        # so lowest chance enemy will be checked first
        return sorted(
            imported_enemies, key=lambda x: x.encounter_chance.value.get()
        )

    def encounter_check(self, enemies: list[str]) -> list[str]:
        """Return enemies after being rng checked."""

        checked_enemies = [
            enemy
            for enemy in enemies
            if rng(enemy.encounter_chance.value.get())
        ]

        return checked_enemies
