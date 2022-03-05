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
    ):
        self.key = convert_to_keys(key)
        self.sector = sector
        self.text = (
            text if text is not None else convert_to_readable(self.key)
        )


class Dialogue:
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

    `dialogue: ({"text": string, ["before": int | float, "after": int | float}])`
    """

    dialogue = []
    dialogue_before = 0
    dialogue_after = 0
    dialogue_speed = 0

    def dispatch(self) -> None:
        """Print dialogue(s) with delay before and/or after."""

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

    entities: ["module.class",]
    """

    entities = []
    sort_by = ""
    check_by = None

    def dispatch(self) -> None:
        entities = self.process_check(self.import_entities())

        for entity in entities:
            self.APP.PROCESS_CLASS(self.APP.MAIN_ACTOR, entity()).flow()

        super().dispatch()

    def import_entities(self) -> list[BaseEntity]:
        """Import entity module from the list `self.entities`."""

        imported_entities = [
            import_from_app(self.APP._APP_NAME, f"entities.{entity}")
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

    def process_check(self, entities: list[str]) -> list[str]:
        """Return entities after being rng checked."""

        checked_entities = [
            entity
            for entity in entities
            if rng(getattr(entity, self.check_by).get())
        ]

        return checked_entities


class SingleEntityProcess(MultipleEntityProcess):
    def process_check(
        self, entities: list[Union[BaseEntity, str]]
    ) -> list[str]:
        checked_entities = super().process_check(entities)

        return (
            [checked_entities[randrange(len(checked_entities))]]
            if checked_entities
            else []
        )
