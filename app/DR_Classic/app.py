from app.DR_Classic.core.exceptions import PlayerDead
from app.DR_Classic.core.process import BattleSequence
from app.DR_Classic.entities.player import Player
from app.DR_Classic.sector.start import MainMenu
from dungeonrun.dungeonrun import DungeonRun


class MyGame(DungeonRun):
    BEGIN_CLASS = MainMenu
    PROCESS_CLASS = BattleSequence
    MAIN_ENTITY = Player

    minotaur = 0
    stone_gargoyle = 0
    boss = 0

    def run(self) -> None:
        try:
            super().run()
        except PlayerDead:
            print("You are dead.")
            print("Game Over.")
            exit(1)
