from time import sleep

from dungeonrun.entity import BaseEntity


class Encounter:
    """
    Basic encounter class.
    """

    def __init__(self, main_actor: BaseEntity, opfor: BaseEntity) -> None:
        self.main_actor = main_actor
        self.opfor = opfor

        self.cycle = 0

        self.intro()

    def display(self) -> None:
        pass

    def intro(self) -> None:
        pass

    def execute(self) -> None:
        sleep(1)
        print("Executed")
