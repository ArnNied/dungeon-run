from dungeonrun.actor.base import BaseActor, Prop, PropWithMax


class Elvish(BaseActor):
    name = Prop("Elvish Class")
    encounter_chance = Prop(0.8)
    health_point = PropWithMax(90, 90)


class Orc(BaseActor):
    name = Prop("Orc Class")
    encounter_chance = Prop(0.7)
    health_point = PropWithMax(120, 120)


class Human(BaseActor):
    name = Prop("Human Class")
    encounter_chance = Prop(0.5)
    health_point = PropWithMax(100, 100)
