from time import sleep

from dungeonrun.dungeonrun import DungeonRun
from dungeonrun.entity import BaseEntity
from dungeonrun.utils import (
    animate,
    convert_to_keys,
    convert_to_readable,
    import_from_pack,
    rng,
)


class BaseSector:
    """
    Basic sector class.

    Note that this class should be inherited first (leftmost) before any sector mixin used.

    `paths: {"sector_key": "module.class"}`
    `path_separator: string`
    """

    paths = None
    path_separator = " :: "

    NEXT_SECTOR = None

    def __init__(self, app: DungeonRun) -> None:
        self.APP = app

        self.before()
        self.dispatch()

    def before(self) -> None:
        pass

    def dispatch(self) -> None:
        pass

    def validate_input(self, sector: str, user_input: str) -> None:
        pass

    def execute(self) -> "BaseSector":
        """Main function to call."""

        self.paths_check()
        while self.NEXT_SECTOR == None:
            self.display_available_path()
            user_input = input("> ")
            sector = self.check_sector(user_input)
            self.validate_input(sector, user_input)

            self.set_next_sector(sector, user_input)

        imported_sector = self.import_next_sector(self.NEXT_SECTOR)

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

    def check_sector(self, user_input: str) -> str:
        chosen_path = convert_to_keys(user_input)

        return self.paths.get(chosen_path, False)

    def set_next_sector(self, sector, user_input) -> None:
        """Set self.next_sector for importing and executing."""

        if sector:
            self.NEXT_SECTOR = sector
        else:
            print(f"Path {user_input} doesn't exist")

    def import_next_sector(self, next_sector: str) -> "BaseSector":
        """Import the class of next sector to instantiate in main.py."""

        return import_from_pack(self.APP._PACK_NAME, f"sector.{next_sector}")


class Dialogue:
    """
    Mixin for Sector to allow printing dialogues to the output.

    `dialogue: ({"text": string, ["before": int | float, "after": int | float}])`
    """

    dialogue = []

    def dispatch(self) -> None:
        """Print dialogue(s) with delay before and/or after."""

        if self.dialogue is not None:
            for line in self.dialogue:
                sleep(line.get("before", 0))
                animate(line["text"])
                sleep(line.get("after", 1))

        super().dispatch()


class MultipleEntityEncounter:
    """

    Class to inherit when a sector will have multiple entity encounter.

    entities: ["module.class",]
    """

    entities = []
    sort_by = ""
    check_by = None

    def dispatch(self) -> None:
        entities = self.encounter_check(self.import_entities())

        for entity in entities:
            entity = entity()
            self.APP.ENCOUNTER_CLASS(self.APP.MAIN_ACTOR, entity).execute()

        super().dispatch()

    def import_entities(self) -> list[BaseEntity]:
        """Import entity module from the list `self.entities`."""

        imported_entities = [
            import_from_pack(self.APP._PACK_NAME, f"entities.{entity}")
            for entity in self.entities
        ]

        # return sorted entity by self.sort_by from lowest
        # so lowest chance entity will be checked first
        if self.sort_by:
            return sorted(
                imported_entities,
                key=lambda x: getattr(x, self.sort_by).get(),
            )
        else:
            return imported_entities

    def encounter_check(self, entities: list[str]) -> list[str]:
        """Return entities after being rng checked."""

        checked_entities = [
            entity
            for entity in entities
            if rng(getattr(entity, self.check_by).get())
        ]

        return checked_entities
