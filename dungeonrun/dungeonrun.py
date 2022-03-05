import inspect
import os

from dungeonrun.entity import BaseEntity
from dungeonrun.exceptions import End
from dungeonrun.process import Process
from dungeonrun.utils import clear_stdout


class DungeonRun:
    """
    Main class as entry point
    """

    PROCESS_CLASS = Process
    BEGIN_CLASS = None
    MAIN_ENTITY = BaseEntity
    END_CLASS = None
    CLEAR_PREVIOUS = True

    def __init__(self) -> None:
        clear_stdout()
        self.prepare()

    def prepare(self) -> None:
        _, app_name = inspect.getmodule(self).__package__.split(".")
        self._APP_NAME = app_name
        self.MAIN_ENTITY = self.MAIN_ENTITY()

    def run(self) -> None:
        sector = self.BEGIN_CLASS(self).execute()

        try:
            while True:
                if self.CLEAR_PREVIOUS:
                    clear_stdout()
                sector = sector(self).execute()
        except End:
            if self.END_CLASS:
                self.END_CLASS(self).execute()
