from dungeonrun.sector.base import BaseSector, MultipleHostileEncounter

class HostileSector(MultipleHostileEncounter, BaseSector):
    paths = {
        "go_south": "SectorOne.South",
        "go_north": "SectorOne.North",
        "go_hostile": "HostileSector.HostileSector"
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
        "Leviathan.Leviathan"
    ]

    def __init__(self, player):
        super().__init__()