from dungeonrun.sector.base import BaseSector, Dialogue

class SectorBegin(Dialogue, BaseSector):
    paths = {
        "go_north": "SectorOne.North"
    }
    dialogue = [
        {
            "text": "hello",
        }
    ]

    def __init__(self, player):
        super().__init__()