class BaseProp:
    def __init__(self, val):
        self.value = val

    def get(self):
        return self.value

    def update(self, val):
        self.value = val

        return self.get()


class Prop:
    def __init__(self, val):
        self.value = BaseProp(val)


class PropWithMax(Prop):
    def __init__(self, starting_value, max_value):
        super().__init__(starting_value)
        self.max_value = BaseProp(max_value)


class BaseActor:
    """
    Class to inherit for actor such as player and enemies
    """

    name = Prop("")
    encounter_chance = Prop(0)
    health_point = PropWithMax(100, 100)

    def name_get(self):
        return self.name

    def hp_get(self):
        return self.health_point
