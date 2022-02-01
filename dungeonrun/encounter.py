from dungeonrun.entity import BaseEntity


class Encounter:
    """
    Basic encounter class.
    """

    def __init__(self, main_actor: BaseEntity, other: BaseEntity) -> None:
        self.main_actor = main_actor
        self.other = other

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
