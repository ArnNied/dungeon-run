from dungeonrun.dungeonrun import DungeonRun

from .core.encounter import MyEncounter
from .sector.HostileSector import HostileSector


class MyGame(DungeonRun):
    BEGIN_CLASS = HostileSector
    ENCOUNTER_CLASS = MyEncounter
