from dungeonrun.sector import (
    DialogueMixin,
    MultipleEntityEncounter,
    SingleEntityEncounter,
)


class CustomMixin:
    check_by = "encounter_chance"
    sort_by = "encounter_chance"


class MultipleEntityEncounter(CustomMixin, MultipleEntityEncounter):
    pass


class SingleEntityEncounter(CustomMixin, SingleEntityEncounter):
    pass


class DialogueMixin(DialogueMixin):
    dialogue_after = 1
    dialogue_speed = 0.014
