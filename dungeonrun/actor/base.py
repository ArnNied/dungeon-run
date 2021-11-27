from typing import Any, Union


class BaseProp:
    def __init__(self, val: Any):
        self.value = val

    def get(self):
        return self.value

    def update(self, val: Any):
        self.value = val

        return self.get()


class Prop:
    """
    A wrapper to use for actor attribute.
    """

    def __str__(self):
        return f"{self.value.get()}"

    def __init__(self, val: Any):
        self.value = BaseProp(val)


class PropWithMax(Prop):
    """
    A wrapper to use for actor attribute that has a max value.
    """

    def __str__(self):
        return f"{self.value.get()}/{self.max_value.get()}"

    def __init__(
        self, starting_value: Union[int, float], max_value: Union[int, float]
    ):
        super().__init__(starting_value)
        self.max_value = BaseProp(max_value)


class BaseActor:
    """
    Class to inherit for actor such as player and enemies.
    """

    name = Prop("")
    encounter_chance = Prop(0)
    health_point = PropWithMax(100, 100)

    visible_prop = (
        {
            "Name": "name",
        },
        {
            "HP": "health_point",
        },
    )

    def display_stat(self):
        for row in range(len(self.visible_prop)):
            stat_row = [
                f"{key}: {getattr(self, val)}"
                for key, val in self.visible_prop[row].items()
            ]

            print("\t".join(stat_row))
