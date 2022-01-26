from dungeonrun.actor import BaseActor, Prop, PropWithMax


class Bipedal(BaseActor):
    visible_prop = (
        {
            "Name": "name",
        },
        {
            "HP": "health_point",
            "STR": "strength",
            "INT": "intellect",
        },
    )


class Elvish(Bipedal):
    name = Prop("Elvish Class")
    encounter_chance = Prop(0.8)
    health_point = PropWithMax(90, 90)
    strength = PropWithMax(0, 2)
    intellect = PropWithMax(5, 10)


class Orc(Bipedal):
    name = Prop("Orc Class")
    encounter_chance = Prop(0.7)
    health_point = PropWithMax(120, 120)
    strength = PropWithMax(5, 10)
    intellect = PropWithMax(0, 2)


class Human(Bipedal):
    name = Prop("Human Class")
    encounter_chance = Prop(0.5)
    health_point = PropWithMax(100, 100)
    strength = PropWithMax(3, 5)
    intellect = PropWithMax(2, 5)
