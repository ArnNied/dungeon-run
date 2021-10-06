from dungeonrun.sector.base import BaseSector, Dialogue

class SectorBegin(Dialogue, BaseSector):
    paths = {
        "go_north": "sector1.North"
    }
    dialogue = [
        {
            "text": "hello",
        }
    ]

    def __init__(self, player):
        super().__init__()