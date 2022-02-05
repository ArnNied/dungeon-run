from dungeonrun.sector import MultipleEntityEncounter, SingleEntityEncounter


class CustomMixin:
    check_by = "encounter_chance"
    sort_by = "encounter_chance"


class MultipleEntityEncounter(CustomMixin, MultipleEntityEncounter):
    pass


class SingleEntityEncounter(CustomMixin, SingleEntityEncounter):
    pass
