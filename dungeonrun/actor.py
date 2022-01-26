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
        self, initial_value: Union[int, float], max_value: Union[int, float]
    ):
        super().__init__(initial_value)
        self.max_value = BaseProp(max_value)


class BaseActor:
    """
    Class to inherit for actor such as player and entities.
    """

    name = Prop("")

    visible_prop = (
        {
            "Name": "name",
        },
    )

    def stringify_prop(self):
        rows = []
        for props in self.visible_prop:
            row = [
                f"{prop_key}: {getattr(self, prop_val)}"
                for prop_key, prop_val in props.items()
            ]

            rows.append("\t".join(row))

        return "\n".join(rows)
