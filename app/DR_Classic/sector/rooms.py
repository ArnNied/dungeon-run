from app.DR_Classic.core.sector import (
    DialogueMixin,
    MultipleEntityProcess,
    SingleEntityProcess,
)
from app.DR_Classic.entities.enemies import Boss, Minotaur, Rat, StoneGargoyle
from dungeonrun.sector import BaseSector, Dialogue, Route


class Intro(DialogueMixin, BaseSector):
    route = Route("rooms.RoomOne")

    dialogue = [
        Dialogue("You wake up in a dark room.\n"),
        Dialogue("You see an unfamiliar roof.\n"),
        Dialogue("You try to get a grasp of your surrounding.\n"),
        Dialogue("Only to be startled by a rat hissing at you.\n", before=2),
    ]

    def execute(self) -> "BaseSector":
        self.APP.PROCESS_CLASS(self.APP.MAIN_ENTITY, Rat()).flow()

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

    # entities = [
    #     "enemies.Rat",
    #     "enemies.BlueSlime",
    # ]


class RoomTwo(DialogueMixin, SingleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomFive", "go_south"),
        Route("rooms.RoomOne", "go_west"),
    ]

    dialogue = [
        Dialogue("You entered a hallway.\n"),
        Dialogue("With dimly lit torches illuminating the surrounding.\n"),
    ]

    # entities = [
    #     "enemies.Rat",
    #     "enemies.Spider",
    # ]


class RoomThree(DialogueMixin, MultipleEntityProcess, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_south"),
        Route("rooms.RoomFive", "go_west"),
    ]

    dialogue = [
        Dialogue("Massive pillar can be seen supporting the ceiling.\n"),
        Dialogue("Piles of bones are scattered across the ground.\n"),
    ]

    # entities = [
    #     "enemies.Skeleton",
    #     "enemies.Skeleton",
    #     "enemies.Skeleton",
    # ]


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

    # entities = [
    #     "enemies.Goblin",
    #     "enemies.Spider",
    #     "enemies.Rat",
    # ]


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

    # entities = [
    #     "enemies.Rat",
    #     "enemies.Spider",
    # ]


class RoomSix(MultipleEntityProcess, DialogueMixin, BaseSector):
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

    # entities = [
    #     "enemies.Goblin",
    #     "enemies.Rat",
    #     "enemies.Spider",
    # ]


class RoomSeven(DialogueMixin, BaseSector):
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


class RoomEight(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_east"),
        Route("rooms.RoomTwelve", "go_south"),
        Route("rooms.RoomSeven", "go_west"),
    ]

    dialogue = [
        Dialogue("The wind from the nearby room picks up the dust\n"),
        Dialogue("Fog is seeping from the floor.\n"),
    ]


class RoomNine(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomThree", "go_north"),
        Route(
            "rooms.RoomThirteen", "go_south", "Go South (MINIBOSS: Minotaur)"
        ),
        Route("rooms.RoomEight", "go_west"),
    ]

    dialogue = [
        Dialogue("The room is massive.\n"),
        Dialogue("A rusty chandelier is hanging from the ceiling.\n"),
    ]


class RoomTen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSix", "go_north"),
        Route("rooms.RoomFourteen", "go_south"),
    ]

    dialogue = [
        Dialogue("You entered a small halway\n"),
        Dialogue("There are cobwebs in the corners.\n"),
    ]


class RoomEleven(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSeven", "go_east"),
        Route("rooms.RoomFourteen", "go_south"),
    ]

    dialogue = [
        Dialogue("The room looks like an armory.\n"),
        Dialogue("Unfortunately all the equipments are broken.\n"),
    ]


class RoomTwelve(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSeven", "go_northwest"),
        Route("rooms.RoomEight", "go_northeast"),
        Route("rooms.RoomSeventeen", "go_south"),
        Route("rooms.RoomFourteen", "go_west"),
    ]

    dialogue = [
        Dialogue("Decayed corpses are piled in the middle of the room.\n"),
        Dialogue("The stench is unbearable.\n"),
    ]


class RoomThirteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomNine", "go_back"),
    ]

    dialogue = [
        Dialogue("MINOTAUR.\n"),
    ]


class RoomFourteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomTen", "go_northwest"),
        Route("rooms.RoomEleven", "go_northeast"),
        Route("rooms.RoomTwelve", "go_east"),
    ]

    dialogue = [
        Dialogue("The room is filled with overgrown vines.\n"),
    ]


class RoomFifteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSixteen", "go_back"),
    ]

    dialogue = [
        Dialogue("GARGOYLE.\n"),
    ]


class RoomSixteen(DialogueMixin, BaseSector):
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


class RoomSeventeen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomTwelve", "go_north"),
        Route("rooms.RoomNineteen", "go_south"),
        Route("rooms.RoomSixteen", "go_west"),
    ]

    dialogue = [
        Dialogue("You entered a long hallway.\n"),
        Dialogue("Broken armor can be seen on their stand.\n"),
    ]


class RoomEighteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSixteen", "go_north"),
        Route("rooms.RoomNineteen", "go_east"),
    ]

    dialogue = [
        Dialogue("Knight statues are standing in a circle.\n"),
        Dialogue("Unknown diagrams painted on the floor.\n"),
    ]


class RoomNineteen(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomSeventeen", "go_north"),
        Route("rooms.RoomTwenty", "go_east", "Go East (FINAL BOSS)"),
        Route("rooms.RoomEighteen", "go_west"),
    ]

    dialogue = [
        Dialogue("A small statue display can be seen in the corner.\n"),
    ]


class RoomTwenty(DialogueMixin, BaseSector):
    route = [
        Route("rooms.RoomNineteen", "go_back"),
    ]

    dialogue = [
        Dialogue("BOSS.\n"),
    ]
