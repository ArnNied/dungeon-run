from dungeonrun.actor.base import BaseActor


class Encounter:
    def __init__(self, player: BaseActor, enemy: BaseActor):
        self.player = player
        self.enemy = enemy

        self.display_interface()

    def display_interface(self) -> None:
        print(
            "========================================================================================================",
            self.enemy.stringify_prop(),
            "",
            self.player.stringify_prop(),
            "========================================================================================================",
            sep="\n",
        )
