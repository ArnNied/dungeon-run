from importlib import import_module
from time import sleep

from dungeonrun.utils import convert_to_readable, convert_to_keys, import_from_pack

class BaseSector:
    """
    Class to inherit when creating an sector.

    Note that this class should be inherited last (rightmost) after any sector mixin used.
    """

    player = None

    paths = None # {"sector_key": "sector_module_location"}
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
    """Class to inherit when a sector need to display dialogue(s)"""

    dialogue = [
        {
            "text": "text here",
            "before": 0,
            "after": 0,
        }
    ]

    def __init__(self):
        if self.dialogue != None:
            for line in self.dialogue:
                # Space between before and after text
                sleep(line.get('before', 0))
                print(line['text'])
                sleep(line.get('after', 1))

        super().__init__()