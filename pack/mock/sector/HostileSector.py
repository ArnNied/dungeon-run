from dungeonrun.sector import BaseSector, Dialogue, MultipleEntityEncounter


class HostileSector(MultipleEntityEncounter, Dialogue, BaseSector):
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

    entities = [
        "Humanoid.Elvish",
        "Humanoid.Orc",
        "Humanoid.Human",
        "Leviathan.Leviathan",
    ]

    sort_by = "encounter_chance"
    check_by = "encounter_chance"
