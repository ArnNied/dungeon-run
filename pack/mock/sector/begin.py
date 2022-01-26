from dungeonrun.sector import BaseSector, Dialogue


class SectorBegin(BaseSector, Dialogue):
    paths = {
        "go_north": "SectorOne.North",
    }
    dialogue = [
        {
            "text": "hello",
        },
    ]

    BaseSector
