import inspect
import random
import time
from random import randrange
from typing import Optional, Union

from dungeonrun.dungeonrun import DungeonRun
from dungeonrun.entity import BaseEntity
from dungeonrun.exceptions import End
from dungeonrun.utils import (
    animate,
    convert_to_keys,
    convert_to_readable,
    import_from_app,
    rng,
)


class BaseSector:
    """
    Basic sector class.

    Note that this class should be inherited last (rightmost) before any sector mixin used.
    """

    route = None
    route_separator = " :: "

    NEXT_SECTOR = None

    def __init__(self, app: DungeonRun) -> None:
        self.APP = app

        self.before()
        self.dispatch()

    def before(self) -> None:
        pass

    def dispatch(self) -> None:
        pass

    def validate_input(self, route: str, user_input: str) -> None:
        return route

    def execute(self) -> "BaseSector":
        """Main function to call."""

        self.route_check()
        while self.NEXT_SECTOR is None:
            self.display_available_route()
            user_input = input("> ")
            route = self.check_route(user_input)
            route = self.validate_input(route, user_input)

            self.set_next_sector(route, user_input)

        imported_sector = self.import_next_sector()

        return imported_sector

    def route_check(self) -> None:
        """
        Check if self.route is a string pointing to a sector.
        OR if self.route is None then it will be considered an 'ending'.
        """

        if self.route is None:
            raise End
        elif isinstance(self.route, Route):
            self.NEXT_SECTOR = self.route

    def display_available_route(self) -> None:
        """Output available route(s) to the terminal."""

        route = [route.text for route in self.route]
        route = self.route_separator.join(route)

        print(f"\n{route}")

    def check_route(self, user_input: str) -> str:
        chosen_route = convert_to_keys(user_input)

        try:
            route = [
                route for route in self.route if route.key == chosen_route
            ][0]
        except IndexError:
            route = False

        return route

    def set_next_sector(
        self, route: Union["Route", str], user_input: str
    ) -> None:
        """Set self.next_sector for importing and executing."""

        if route:
            self.NEXT_SECTOR = route
        else:
            print(f"Route {user_input} does not exist")

    def import_next_sector(self) -> "BaseSector":
        """Import the class of next sector to instantiate in main.py."""

        sector = self.NEXT_SECTOR.sector
        if type(sector) is str:
            return import_from_app(self.APP._APP_NAME, f"sector.{sector}")
        else:
            return sector


class Route:
    def __init__(
        self, sector: Union["BaseSector", str], key: str = "", text=None
    ) -> "Route":
        self.key = convert_to_keys(key)
        self.sector = sector
        self.text = (
            text if text is not None else convert_to_readable(self.key)
        )


class Dialogue:
    """
    Class needed for `DialogueMixin`. Will use `Dialogue` configuration if supplied when initiated,
    else it will use the `DialogueMixin` configuration

    `before`: Union[int, float] = None | Amount of delay before printing current dialogue

    `after`: Union[int, float] = None | Amount of delay after printing current dialogue

    `speed`: Union[int, float] = None | Amount of delay between character (0 means the text is printed instantly)
    """

    def __init__(
        self,
        dialogue: str,
        before: Optional[Union[int, float]] = None,
        after: Optional[Union[int, float]] = None,
        speed: Optional[Union[int, float]] = None,
    ) -> None:
        self.dialogue = dialogue
        self.before = before
        self.after = after
        self.speed = speed

    def display(
        self,
        before: Union[int, float] = None,
        after: Union[int, float] = None,
        speed: Union[int, float] = None,
    ) -> None:
        time.sleep(self.before if self.before is not None else before or 0)
        animate(
            f"{self.dialogue}",
            self.speed if self.speed is not None else speed or 0,
        )
        time.sleep(self.after if self.after is not None else after or 0)


class DialogueMixin:
    """
    Mixin for Sector to allow printing dialogues to the output.

    `dialogue`: list[Dialogue] | A list of dialogue to be printed

    `dialogue_before`: Union[int, float] = 0 | Amount of delay before printing current dialogue

    `dialogue_after`: Union[int, float] = 0 | Amount of delay after printing current dialogue

    `dialogue_speed`: Union[int, float] = 0 | Amount of delay between character (0 means the text is printed instantly)

    """

    dialogue = []
    dialogue_before = 0
    dialogue_after = 0
    dialogue_speed = 0

    def dispatch(self) -> None:
        """Prints the dialogue with the configured attribute."""

        if self.dialogue is not None:
            for line in self.dialogue:
                line.display(
                    self.dialogue_before,
                    self.dialogue_after,
                    self.dialogue_speed,
                )

        super().dispatch()


class MultipleEntityProcess:
    """
    Class to inherit when a sector will have multiple entity process.

    `entities`: list[Union[str, BaseEntity]]

    `sort_by`: str | Entities will be sorted by this attibute name

    `check_by`: Optional[str] = None | If entities need to be checked by a rng from `utils.random()`
    """

    entities = []
    sort_by = None
    check_by = None

    def dispatch(self) -> None:
        entities = self.import_entities()
        if self.check_by is not None:
            entities = self.process_check(entities)

        for entity in entities:
            self.APP.PROCESS_CLASS(self.APP.MAIN_ENTITY, entity()).execute()

        super().dispatch()

    def import_entities(self) -> list[BaseEntity]:
        """Import entity module from the list `self.entities`."""

        imported_entities = []
        for entity in self.entities:
            if type(entity) is str:
                imported_entities.append(
                    import_from_app(self.APP._APP_NAME, f"entities.{entity}")
                )
            else:
                imported_entities.append(entity)

        # return sorted entity by self.sort_by from lowest
        # so lowest chance entity will be checked first
        if self.sort_by:
            return sorted(
                imported_entities,
                key=lambda x: getattr(x, self.sort_by).get(),
            )
        else:
            return imported_entities

    def process_check(self, entities: list[str]) -> list[str]:
        """Return entities after being rng checked."""

        checked_entities = [
            entity
            for entity in entities
            if rng(getattr(entity, self.check_by).get())
        ]

        return checked_entities


class SingleEntityProcess(MultipleEntityProcess):
    """
    Class to inherit when a sector will have single entity process.

    `entities`: list[Union[str, BaseEntity]]

    `sort_by`: str | Entities will be sorted by this attibute name

    `check_by`: Optional[str] = None | If entities need to be checked by a rng from `utils.random()`

    `random`: int = 0 | Return a random entity or the first one
    """

    random = 0

    def import_entities(self) -> list[BaseEntity]:
        imported_entities = super().import_entities()

        try:
            if self.random:
                return [random.choice(imported_entities)]
            else:
                return [imported_entities[0]]
        except IndexError:
            return []
