import inspect
import os
from importlib import import_module

from dungeonrun.actor import BaseActor
from dungeonrun.encounter import Encounter


class DungeonRun:
    ENCOUNTER_CLASS = Encounter
    BEGIN_CLASS = None
    MAIN_ACTOR = BaseActor

    def __init__(self):
        self.prepare()

    def prepare(self):
        os.system("cls" if os.name == "nt" else "clear")

        _, pack_name = inspect.getmodule(self).__package__.split(".")
        self._PACK_NAME = pack_name

    def run(self):
        sector = self.BEGIN_CLASS(self, self.MAIN_ACTOR).execute()

        while True:
            os.system("cls")
            sector = sector(self, self.MAIN_ACTOR).execute()
