from app.DR_Classic.core.sector import DialogueMixin
from dungeonrun.sector import BaseSector, Dialogue, Route


class One(DialogueMixin, BaseSector):
    dialogue_speed = 0.05
    dialogue_after = 2

    route = Route("endings.Credits")

    dialogue = [
        Dialogue("You escaped through the door.\n"),
        Dialogue("A stair can be seen leading up.\n"),
        Dialogue("You start making your way up the stairs.\n"),
        Dialogue("After what feels like hours, you can see sunlight.\n"),
        Dialogue("You make haste your footstep.\n"),
        Dialogue("You finally reached the top.\n"),
        Dialogue("Only to be greeted with barren"),
        Dialogue(", destroyed world.\n"),
        Dialogue("With monsters seen near mankind remains.\n", after=5),
    ]


class Two(DialogueMixin, BaseSector):
    dialogue_speed = 0.05
    dialogue_after = 2

    route = Route("endings.Credits")

    dialogue = [
        Dialogue("You looked at the door in front of you.\n"),
        Dialogue("You hesitantly touch its surface.\n"),
        Dialogue("After a few seconds of thought you decide to let go.\n", 5),
        Dialogue("Then"),
        Dialogue(", you feel a rumbling underneath your feet.\n"),
        Dialogue("While black fog starts to appear from the walls"),
        Dialogue(", fully enveloping your body.\n"),
        Dialogue(
            "t h e  d u n g e o n  h a s  a c k n o w l e d g e s  y o u.\n",
            4,
            5,
            0.2,
        ),
    ]


class Credits(DialogueMixin, BaseSector):
    dialogue = [
        Dialogue("Dungeon Run Classic\n"),
        Dialogue("Made by \"Andrien 'ArnNied' Wiandyano\"\n"),
        Dialogue("Github: http://github.com/ArnNied\n"),
        Dialogue("Source code: http://github.com/ArnNied/dungeon-run\n"),
        Dialogue("Thank you for playing :)\n"),
    ]
