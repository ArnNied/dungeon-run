from dungeonrun.dungeonrun import DungeonRun

from .core.encounter import MyEncounter
from .entities.player import Player
from .sector.start import MainMenu


class MyGame(DungeonRun):
    BEGIN_CLASS = MainMenu
    ENCOUNTER_CLASS = MyEncounter
    MAIN_ACTOR = Player
