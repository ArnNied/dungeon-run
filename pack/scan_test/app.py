from dungeonrun.dungeonrun import DungeonRun

from .core.encounter import MyEncounter
from .sector.Begin import SectorBegin


class MyGame(DungeonRun):
    BEGIN_CLASS = SectorBegin
    # SECTOR_BEGIN = "HostileSector.HostileSector"
    ENCOUNTER_CLASS = MyEncounter
