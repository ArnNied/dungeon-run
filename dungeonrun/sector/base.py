from importlib import import_module
from time import sleep

from dungeonrun.utils import convert_to_readable, convert_to_keys, import_from_pack, rng

class BaseSector:
    """
    Class to inherit when creating an sector.

    Note that this class should be inherited last (rightmost) after any sector mixin used.

    paths: {"sector_key": "module.class"}
    """

    player = None

    paths = None
    path_separator = " :: "

    next_sector = None

    def __init__(self):
        super().__init__()

    def execute(self):
        """Main function to call"""

        self.paths_check()
        while self.next_sector == None:
            self.display_available_path()
            self.set_next_sector()

        imported_sector = self.import_next_sector(self.next_sector)

        return imported_sector

    def paths_check(self):
        """
        Check if self.paths is a string pointing to an sector
        OR if self.paths is None then it will be considered an 'ending'
        """

        if self.paths == None:
            print("end")
        elif type(self.paths) is str:
            self.next_sector = self.paths
        # elif self.paths is None:
        #     raise exc.PathsImproperlyConfigured

    def display_available_path(self):
        """Convert underscore style to space for human read"""

        paths = []
        for path in self.paths:
            paths.append(convert_to_readable(path))

        paths = self.path_separator.join(paths)
        print(f"\n{paths}")

    def set_next_sector(self):
        """Set self.next_sector for importing and executing"""

        player_choice = input("> ")

        # Convert from human-readable (user input) to dictionary keys for self.paths use
        chosen_path = convert_to_keys(player_choice)
        chosen_path = self.paths.get(chosen_path, False)

        if chosen_path == False:
            print(f"Path {player_choice} doesn't exist")
        else:
            self.next_sector = chosen_path

    def import_next_sector(self, next_sector):
        """Import the class of next sector to instantiate in main.py"""

        return import_from_pack(f'sector.{next_sector}')


class Dialogue:
    """
    Class to inherit when a sector need to display dialogue(s)

    dialogue: [{"text": string, "before": int|float, "after": int|float},]
    """

    dialogue = []

    def __init__(self):
        """Print dialogue(s) with delay before and/or after"""

        if self.dialogue != None:
            for line in self.dialogue:
                sleep(line.get('before', 0))
                print(line['text'])
                sleep(line.get('after', 1))

        super().__init__()

class MultipleHostileEncounter:
    """
    Class to inherit when a sector will have multiple enemy encounter

    enemies: ["module.class",]
    """

    enemies = []

    def __init__(self):
        enemies = self.encounter_check(self.import_enemies())

        for enemy in enemies:
            print(f"encountered {enemy.name}")

        super().__init__()

    def import_enemies(self):
        """Import enemy module from the list self.enemies"""

        imported_enemies = []

        for enemy in self.enemies:
            # import enemy module
            imported_enemies.append(import_from_pack(f"enemies.{enemy}"))

        # return sorted enemy by encounter_chance from lowest
        # so lowest chance enemy will be checked first
        return sorted(imported_enemies, key=lambda x: x.encounter_chance)

    def encounter_check(self, enemies):
        """Return enemies after being rng checked"""

        checked_enemies = [enemy for enemy in enemies if rng() <= enemy.encounter_chance]
        # for enemy in enemies:
        #     if rng() <= enemy.encounter_chance:
        #         checked_enemies.append(enemy)

        return checked_enemies