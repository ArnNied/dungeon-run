from dungeonrun.sector.base import (
    BaseSector,
    Dialogue,
    MultipleHostileEncounter,
)


class HostileSector(MultipleHostileEncounter, Dialogue, BaseSector):
    paths = {
        "go_south": "SectorOne.South",
        "go_north": "SectorOne.North",
        "go_hostile": "HostileSector.HostileSector",
    }

    dialogue = [
        {
            "text": "entered hostile sector",
        }
    ]

    enemies = [
        "Humanoid.Elvish",
        "Humanoid.Orc",
        "Humanoid.Human",
        "Leviathan.Leviathan",
    ]

