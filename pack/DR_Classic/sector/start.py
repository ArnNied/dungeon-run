import time

from dungeonrun.sector import BaseSector, Route


class MainMenu(BaseSector):
    route = [
        Route("start.AllocateSTR", "play"),
        Route("start.QuitGame", "quit"),
    ]

    def before(self):
        print(
            """
  _____                                       _____
 |  __ \                                     |  __ \\
 | |  | |_   _ _ __   __ _  ___  ___  _ __   | |__) |   _ _ __
 | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  |  _  / | | | '_ \\
 | |__| | |_| | | | | (_| |  __/ (_) | | | | | | \ \ |_| | | | |
 |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_| |_|  \_\__,_|_| |_|
                      __/ |
   _____ _           |___/
  / ____| |             (_)
 | |    | | __ _ ___ ___ _  ___
 | |    | |/ _` / __/ __| |/ __|
 | |____| | (_| \__ \__ \ | (__
  \_____|_|\__,_|___/___/_|\___|

              """
        )


class AllocateSTR(BaseSector):
    def __init__(self, app):
        super().__init__(app)
        self.APP.starting_points = 8

    @property
    def route(self):
        return [
            Route(
                "",
                text=f"Enter a number between 0-{self.APP.starting_points} for your STR:",
            )
        ]

    def validate_input(self, sector: str, user_input: str) -> None:
        try:
            user_input = int(user_input)
            if 0 <= user_input <= self.APP.starting_points:
                self.APP.MAIN_ACTOR.strength.update(user_input)
                self.APP.starting_points -= user_input
                return Route("start.AllocateAGI")

        except ValueError:
            pass

        print("Error: Invalid input")
        time.sleep(1)

        return Route("start.AllocateSTR")

    def execute(self):
        print(
            "===================================================================================="
        )
        print(
            f"You have {self.APP.starting_points} unallocated Skill Points."
        )
        print(
            "STR affect your damage reduction and the damage you dealt (primarily axes)."
        )

        return super().execute()


class AllocateAGI(BaseSector):
    @property
    def route(self):
        return [
            Route(
                "",
                f"Enter a number between 0-{self.APP.starting_points} for your AGI:",
            )
        ]

    def validate_input(self, sector: str, user_input: str) -> None:
        try:
            user_input = int(user_input)
            if 0 <= user_input <= self.APP.starting_points:
                self.APP.MAIN_ACTOR.agility.update(user_input)
                self.APP.starting_points -= user_input
                return Route("start.AllocateMISC")

        except ValueError:
            pass

        print("Error: Invalid input")
        time.sleep(1)

        return Route("start.AllocateAGI")

    def execute(self):
        print(
            "===================================================================================="
        )
        print(
            f"You have {self.APP.starting_points} unallocated Skill Points."
        )
        print("AGI affect your evade and hit chance (primarily swords).")

        return super().execute()


class AllocateMISC(BaseSector):
    @property
    def route(self):
        return [
            Route(
                "",
                f"Enter a number between 0-{self.APP.starting_points} for your MISC:",
            )
        ]

    def validate_input(self, sector: str, user_input: str) -> None:
        try:
            user_input = int(user_input)
            if 0 <= user_input <= self.APP.starting_points:
                self.APP.MAIN_ACTOR.misc.update(user_input)
                self.APP.starting_points -= user_input
                return Route("start.Confirmation")

        except ValueError:
            pass

        print("Error: Invalid input")
        time.sleep(1)

        return Route("start.AllocateMISC")

    def execute(self):
        print(
            "===================================================================================="
        )
        print(
            f"You have {self.APP.starting_points} unallocated Skill Points."
        )
        print(
            "MISC skill will increase potion effectiveness, affect your chances of making a parry, and critical (primarily rapiers)"
        )

        return super().execute()


class Confirmation(BaseSector):
    route = [
        Route("rooms.Intro", "confirm"),
        Route("start.AllocateSTR", "restart"),
    ]

    def execute(self):
        if self.APP.starting_points:
            print(
                f"You have {self.APP.starting_points} unallocated Skill Points.\n"
            )

        print("You will start with these stats")
        print("====================")
        print(self.APP.MAIN_ACTOR.stringify_prop())

        return super().execute()


class QuitGame(BaseSector):
    paths = None
