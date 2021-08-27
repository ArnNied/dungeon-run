from importlib import import_module
from time import sleep

from dungeonrun.utils import convert_to_readable, convert_to_keys, import_from_pack
from dungeonrun.area import exceptions as exc

class BaseArea:
    """
    Class to inherit when creating an area.
    
    Note that this class should be inherited last (rightmost) after any area mixin used.
    """

    player = None
    paths = None # {"area_key": "area_module_location"}
    next_area = None
    path_separator = " :: "

    def __init__(self):
        super().__init__()

    # def attribute_check(self):
    #     if type(self.paths) is not str or type(self.paths) is not dict or type(self.paths) is not None:
    #         pass # Raise paths improper
    #     if type(self.path_separator) is not str:
    #         pass 
    
    def execute(self):
        """Main function to call"""

        self.paths_check()
        while self.next_area == None:
            self.display_available_path()
            self.set_next_area()

        imported_area = self.import_next_area(self.next_area)

        return imported_area

    def paths_check(self):
        """Check if self.paths is a string pointing to an area
        OR if self.paths is None then it will be considered an 'ending'"""

        if self.paths == 'end':
            raise exc.End
        elif type(self.paths) is str:
            self.next_area = self.paths
        # elif self.paths is None:
        #     raise exc.PathsImproperlyConfigured

    def display_available_path(self):
        """Convert underscore style to space for human read"""
        
        paths = []
        for path in self.paths:
            paths.append(convert_to_readable(path))

        paths = self.path_separator.join(paths)
        print(f"\n{paths}")

    def set_next_area(self):
        """Set self.next_area for importing and executing"""

        player_choice = input("> ")

        # Convert from human-readable (user input) to dictionary keys for self.paths use
        chosen_path = convert_to_keys(player_choice)
        chosen_path = self.paths.get(chosen_path, False)

        if chosen_path == False:
            print(f"Path {player_choice} doesn't exist")
        else:
            self.next_area = chosen_path

    def import_next_area(self, next_area):
        """Import the class of next area to instantiate in main.py"""
        
        return import_from_pack(f'area.{next_area}')


class Dialogue:
    """Class to be imported when an area need to display dialogue(s)"""

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
