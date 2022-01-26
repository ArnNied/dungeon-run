from time import sleep

from dungeonrun.actor import BaseActor


class Encounter:
    def __init__(self, player: BaseActor, opfor: BaseActor):
        self.player = player
        self.opfor = opfor

        self.cycle = 0

        self.intro()

    def intro(self):
        print(f"encountered {self.opfor.name.value.get()}")

    def execute(self):
        print("Executed")
