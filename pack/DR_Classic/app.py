from dungeonrun.dungeonrun import DungeonRun
from pack.DR_Classic.core.encounter import BattleSequence
from pack.DR_Classic.core.exceptions import PlayerDead
from pack.DR_Classic.entities.player import Player
from pack.DR_Classic.sector.start import MainMenu


class MyGame(DungeonRun):
    BEGIN_CLASS = MainMenu
    ENCOUNTER_CLASS = BattleSequence
    MAIN_ACTOR = Player

    def run(self) -> None:
        try:
            super().run()
        except PlayerDead:
            print("You are dead.")
            print("Game Over.")
            exit(1)
