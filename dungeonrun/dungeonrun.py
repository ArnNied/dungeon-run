import inspect
import os

from dungeonrun.encounter import Encounter
from dungeonrun.entity import BaseEntity
from dungeonrun.exceptions import End
from dungeonrun.utils import clear_stdout


class DungeonRun:
    """
    Main class as entry point
    """

    ENCOUNTER_CLASS = Encounter
    BEGIN_CLASS = None
    MAIN_ACTOR = BaseEntity
    END_CLASS = None

    def __init__(self) -> None:
        clear_stdout()
        self.prepare()

    def prepare(self) -> None:
        _, pack_name = inspect.getmodule(self).__package__.split(".")
        self._PACK_NAME = pack_name
        self.MAIN_ACTOR = self.MAIN_ACTOR()

    def run(self) -> None:
        sector = self.BEGIN_CLASS(self).execute()

        try:
            while True:
                clear_stdout()
                sector = sector(self).execute()
        except End:
            if self.END_CLASS:
                self.END_CLASS(self).execute()
