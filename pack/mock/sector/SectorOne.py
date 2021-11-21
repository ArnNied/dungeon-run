from dungeonrun.sector.base import BaseSector, Dialogue


class North(Dialogue, BaseSector):
    paths = {
        "go_south": "SectorOne.South",
        "go_hostile": "HostileSector.HostileSector",
    }

    dialogue = [{"text": "You're in the north sector"}]

    def __init__(self, player):
        super().__init__()


class South(Dialogue, BaseSector):
    paths = {
        "go_north": "SectorOne.North",
        "go_hostile": "HostileSector.HostileSector",
    }

    dialogue = [{"text": "You're in the south sector"}]

    def __init__(self, player):
        super().__init__()
