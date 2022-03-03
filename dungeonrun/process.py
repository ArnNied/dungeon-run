from dungeonrun.entity import BaseEntity


class Process:
    """
    Basic process class.
    """

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def flow(self) -> None:
        self.before()
        self.execute()
        self.after()

    def before(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def after(self) -> None:
        pass
