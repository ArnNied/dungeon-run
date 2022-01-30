from dungeonrun.sector import BaseSector, Dialogue, MultipleEntityEncounter


class Intro(Dialogue, BaseSector):
    paths = {
        "go_back": "start.AllocateSTR",
        "quit": "start.QuitGame",
    }

    dialogue = [
        {"text": "You wake up in a dark room"},
        {"text": "You see an unfamiliar roof"},
        {"text": "You try to get a grasp of your surrounding"},
        {"text": "Only to be startled by a rat hissing at you"},
    ]
