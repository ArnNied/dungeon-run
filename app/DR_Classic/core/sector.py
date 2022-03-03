from dungeonrun.sector import (
    DialogueMixin,
    MultipleEntityProcess,
    SingleEntityProcess,
)


class CustomMixin:
    check_by = "process_chance"
    sort_by = "process_chance"


class MultipleEntityProcess(CustomMixin, MultipleEntityProcess):
    pass


class SingleEntityProcess(CustomMixin, SingleEntityProcess):
    pass


class DialogueMixin(DialogueMixin):
    dialogue_after = 1
    dialogue_speed = 0.014
