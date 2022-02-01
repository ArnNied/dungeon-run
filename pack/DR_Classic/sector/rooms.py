from dungeonrun.sector import (
    BaseSector,
    Dialogue,
    DialogueMixin,
    MultipleEntityEncounter,
)


class Intro(DialogueMixin, MultipleEntityEncounter, BaseSector):
    paths = {
        "repeat": "rooms.Intro",
        "go_back": "start.AllocateSTR",
        "quit": "start.QuitGame",
    }

    dialogue = [
        Dialogue("You wake up in a dark room.\n"),
        Dialogue("You see an unfamiliar roof.\n"),
        Dialogue("You try to get a grasp of your surrounding.\n"),
        Dialogue("Only to be startled by a rat hissing at you.\n", before=2),
    ]

    entities = ["enemies.Spider"]
    check_by = "encounter_chance"
