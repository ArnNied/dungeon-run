from dungeonrun.entity import BaseEntity


class Process:
    """
    Basic process class.
    """

    def __init__(self, **kwargs) -> "Process":
        for key, value in kwargs.items():
            setattr(self, key, value)

    def execute(self) -> None:
        return True
