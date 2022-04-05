import time

from app.DR_Classic.core.process import LootEvent
from app.DR_Classic.core.sector import (
    DialogueMixin,
    MultipleEntityProcess,
    SingleEntityProcess,
)
from app.DR_Classic.entities.apparel import HeavyThree, LightThree
from app.DR_Classic.entities.enemies import Boss, Minotaur, Rat, StoneGargoyle
from dungeonrun.sector import BaseSector, Dialogue, Route
from dungeonrun.utils import import_from_app


class Intro(DialogueMixin, BaseSector):
    route = Route("rooms.RoomOne")

    dialogue = [
        Dialogue("You wake up in a dark room.\n"),
        Dialogue("You see an unfamiliar roof.\n"),
        Dialogue("You try to get a grasp of your surrounding.\n"),
        Dialogue("Only to be startled by a rat hissing at you.\n", before=2),
    ]

    def execute(self) -> "BaseSector":
        self.APP.PROCESS_CLASS(self.APP.MAIN_ENTITY, Rat()).execute()

        return super().execute()


class RoomOne(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomTwo", "go_east"),
        Route("rooms.RoomSix", "go_south"),
    ]

    dialogue = [
        Dialogue("You are standing in a brightly lit room.\n"),
        Dialogue(
            "With unidentifiable floating light source hanging from the ceiling.\n"
        ),
        Dialogue("You see a compass carved in the middle of the floor\n"),
    ]

    entities = [
        "enemies.Rat",
        "enemies.BlueSlime",
    ]


class RoomTwo(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomFive", "go_south"),
        Route("rooms.RoomOne", "go_west"),
    ]

    dialogue = [
        Dialogue("You entered a hallway.\n"),
        Dialogue("With dimly lit torches illuminating the surrounding.\n"),
    ]

    entities = [
        "enemies.Rat",
        "enemies.Spider",
    ]


class RoomThree(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_south"),
        Route("rooms.RoomFive", "go_west"),
    ]

    dialogue = [
        Dialogue("The room is massive.\n"),
        Dialogue("A rusty chandelier is hanging from the ceiling.\n"),
    ]

    entities = [
        "enemies.Goblin",
        "enemies.Spider",
    ]


class RoomFour(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomFive", "go_east"),
        Route("rooms.RoomSeven", "go_south"),
        Route("rooms.RoomSix", "go_west"),
    ]

    dialogue = [
        Dialogue("The air feels thick and heavy.\n"),
        Dialogue("Cracks can be seen across the wall.\n"),
    ]

    entities = [
        "enemies.Goblin",
        "enemies.Spider",
        "enemies.Rat",
    ]


class RoomFive(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomTwo", "go_north"),
        Route("rooms.RoomThree", "go_east"),
        Route("rooms.RoomFour", "go_west"),
    ]

    dialogue = [
        Dialogue("Various markings can be seen on the wall.\n"),
        Dialogue("You have no idea what they are.\n"),
    ]

    entities = [
        "enemies.Rat",
        "enemies.Goblin",
    ]


class RoomSix(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomOne", "go_north"),
        Route("rooms.RoomFour", "go_northeast"),
        Route("rooms.RoomSeven", "go_southeast"),
        Route("rooms.RoomTen", "go_south"),
    ]

    dialogue = [
        Dialogue("There are 4 passage available.\n"),
        Dialogue("Each marked with unknown symbol.\n"),
    ]

    entities = [
        "enemies.Goblin",
        "enemies.Rat",
        "enemies.Spider",
    ]


class RoomSeven(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomFour", "go_north"),
        Route("rooms.RoomEight", "go_east"),
        Route("rooms.RoomTwelve", "go_south"),
        Route("rooms.RoomEleven", "go_southwest"),
        Route("rooms.RoomSix", "go_northwest"),
    ]

    dialogue = [
        Dialogue("You felt the wind coming from the ceiling.\n"),
        Dialogue(
            "Slimy substances can be seen along the walls and floors.\n"
        ),
    ]

    entities = [
        "enemies.RedSlime",
        "enemies.GreenSlime",
    ]


class RoomEight(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_east"),
        Route("rooms.RoomTwelve", "go_south"),
        Route("rooms.RoomSeven", "go_west"),
    ]

    dialogue = [
        Dialogue("The wind from the nearby room picks up the dust\n"),
    ]

    entities = [
        "enemies.Skeleton",
        "enemies.GreenSlime",
    ]


class RoomNine(DialogueMixin, MultipleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomThree", "go_north"),
        Route(
            "rooms.RoomThirteen", "go_south", "Go South (MINIBOSS: Minotaur)"
        ),
        Route("rooms.RoomEight", "go_west"),
    ]

    dialogue = [
        Dialogue("Massive pillar can be seen supporting the ceiling.\n"),
        Dialogue("Piles of bones are scattered across the ground.\n"),
    ]

    entities = [
        "enemies.Skeleton",
        "enemies.Skeleton",
        "enemies.Skeleton",
    ]


class RoomTen(DialogueMixin, MultipleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSix", "go_north"),
        Route("rooms.RoomFourteen", "go_south"),
    ]

    dialogue = [
        Dialogue("You entered a small halway\n"),
        Dialogue("There are cobwebs in the corners.\n"),
    ]

    entities = [
        "enemies.Spider",
        "enemies.Skeleton",
    ]


class RoomEleven(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSeven", "go_east"),
        Route("rooms.RoomFourteen", "go_south"),
    ]

    dialogue = [
        Dialogue("The room looks like an armory.\n"),
        Dialogue("Unfortunately all the equipments are broken.\n"),
    ]

    entities = [
        "enemies.Goblin",
        "enemies.Skeleton",
    ]


class RoomTwelve(DialogueMixin, MultipleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSeven", "go_northwest"),
        Route("rooms.RoomEight", "go_northeast"),
        Route("rooms.RoomSeventeen", "go_south"),
        Route("rooms.RoomFourteen", "go_west"),
    ]

    dialogue = [
        Dialogue("Decaying corpses are piled in the middle of the room.\n"),
        Dialogue("The stench is unbearable.\n"),
    ]

    entities = [
        "enemies.Zombie",
        "enemies.Zombie",
        "enemies.Skeleton",
    ]


class RoomThirteen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_back"),
    ]

    dialogue = [
        Dialogue("A giant minotaur is sitting on a throne.\n"),
        Dialogue("It noticed your presence.\n"),
    ]

    def execute(self) -> "BaseSector":
        result = self.APP.PROCESS_CLASS(
            self.APP.MAIN_ENTITY, Minotaur()
        ).execute()

        if not result:
            return import_from_app(
                self.APP._APP_NAME, "sector.rooms.RoomNine"
            )
        else:
            self.APP.minotaur = 1
            print(f"{Minotaur.name.get()} dropped a {HeavyThree.name.get()}")
            LootEvent(self.APP.MAIN_ENTITY).handle_drop(HeavyThree)

        return super().execute()


class RoomFourteen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomTen", "go_northwest"),
        Route("rooms.RoomEleven", "go_northeast"),
        Route("rooms.RoomTwelve", "go_east"),
    ]

    dialogue = [
        Dialogue("The room is filled with overgrown vines.\n"),
    ]

    entities = [
        "enemies.GreenSlime",
        "enemies.Skeleton",
        "enemies.Spider",
    ]


class RoomFifteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSixteen", "go_back"),
    ]

    dialogue = [
        Dialogue("A room full of treasure greets your eyes.\n"),
        Dialogue("Winged statue encircles the room.\n"),
        Dialogue("One of them started moving.\n"),
    ]

    def execute(self) -> "BaseSector":
        result = self.APP.PROCESS_CLASS(
            self.APP.MAIN_ENTITY, StoneGargoyle()
        ).execute()

        if not result:
            return import_from_app(
                self.APP._APP_NAME, "sector.rooms.RoomSixteen"
            )
        else:
            self.APP.stone_gargoyle = 1
            print(
                f"{StoneGargoyle.name.get()} dropped a {LightThree.name.get()}"
            )
            LootEvent(self.APP.MAIN_ENTITY).handle_drop(LightThree)

        return super().execute()


class RoomSixteen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSeventeen", "go_east"),
        Route("rooms.RoomEighteen", "go_south"),
        Route(
            "rooms.RoomFifteen",
            "go_west",
            "Go West (MINIBOSS: Stone Gargoyle)",
        ),
    ]

    dialogue = [
        Dialogue("Pieces of broken vases are scattered on the floor.\n"),
    ]

    entities = [
        "enemies.Zombie",
        "enemies.GreenSlime",
    ]


class RoomSeventeen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomTwelve", "go_north"),
        Route("rooms.RoomNineteen", "go_south"),
        Route("rooms.RoomSixteen", "go_west"),
    ]

    dialogue = [
        Dialogue("You entered a long hallway.\n"),
        Dialogue("Broken armor can be seen on their stand.\n"),
    ]

    entities = [
        "enemies.Zombie",
        "enemies.FallenPaladin",
    ]


class RoomEighteen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSixteen", "go_north"),
        Route("rooms.RoomNineteen", "go_east"),
    ]

    dialogue = [
        Dialogue("Knight statues are standing in a circle.\n"),
        Dialogue("Unknown diagrams painted on the floor.\n"),
    ]

    entities = [
        "enemies.Zombie",
        "enemies.HollowKnight",
    ]


class RoomNineteen(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomSeventeen", "go_north"),
        Route("rooms.RoomTwenty", "go_east", "Go East (FINAL BOSS)"),
        Route("rooms.RoomEighteen", "go_west"),
    ]

    dialogue = [
        Dialogue("A small statue display can be seen in the corner.\n"),
    ]

    entities = [
        "enemies.Zombie",
        "enemies.RedSlime",
    ]


class RoomTwenty(DialogueMixin, BaseSector):
    route = [
        Route("endings.One", "escape"),
        Route("endings.Two", "stay"),
    ]

    @property
    def dialogue(self):
        dialogue = [
            Dialogue("You come accross an eerie looking door.\n"),
            Dialogue("With two round orb implanted to each of its side.\n"),
        ]

        if not self.APP.minotaur and not self.APP.stone_gargoyle:
            dialogue.append(Dialogue("Both of them are blacked out.\n"))
        elif self.APP.minotaur and self.APP.stone_gargoyle:
            dialogue.append(Dialogue(f"Both of them are lit up\n"))
        else:
            dialogue.append(Dialogue("One of them is lit up.\n"))

        if not self.APP.minotaur or not self.APP.stone_gargoyle:
            dialogue.append(
                Dialogue("The door won't budge no mater how hard you try.\n")
            )
        else:
            dialogue.append(Dialogue("The door opened in your presence.\n"))
            dialogue.append(
                Dialogue(
                    "You are greeted with a shadowy figure guarding a door.\n",
                    1,
                )
            )
            dialogue.append(
                Dialogue(
                    "You feel a glimpse of hope coming from that door.\n", 1
                )
            )

        return dialogue

    def execute(self) -> "BaseSector":
        if self.APP.minotaur and self.APP.stone_gargoyle:
            result = self.APP.PROCESS_CLASS(
                self.APP.MAIN_ENTITY, Boss()
            ).execute()

            if not result:
                return import_from_app(
                    self.APP._APP_NAME, "sector.rooms.RoomNineteen"
                )
            else:
                self.APP.boss = 1
        else:
            time.sleep(2)
            return import_from_app(
                self.APP._APP_NAME, "sector.rooms.RoomNineteen"
            )

        return super().execute()
