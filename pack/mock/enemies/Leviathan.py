from dungeonrun.actor.base import BaseActor, Prop, PropWithMax


class Leviathan(BaseActor):
    name = Prop("Leviathan Class")
    encounter_chance = Prop(0.1)
