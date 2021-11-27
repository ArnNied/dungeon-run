from dungeonrun.sector.base import BaseSector, Dialogue


class North(BaseSector, Dialogue):
    paths = {
        "go_south": "SectorOne.South",
        "go_hostile": "HostileSector.HostileSector",
    }

    dialogue = [
        {
            "text": "You're in the north sector",
        },
    ]

    def __init__(self, player):
        super().__init__(player)


class South(BaseSector, Dialogue):
    paths = {
        "go_north": "SectorOne.North",
        "go_hostile": "HostileSector.HostileSector",
    }

    dialogue = [
        {
            "text": "You're in the south sector",
        },
    ]

    def __init__(self, player):
        super().__init__(player)
