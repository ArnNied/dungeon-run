from dungeonrun.actor.base import BaseActor, Prop, PropWithMax


class TitanClass(BaseActor):
    visible_prop = (
        {
            "Name": "name",
        },
        {
            "Class": "species_class",
        },
        {
            "HP": "health_point",
            "STR": "strength",
            "INT": "intellect",
        },
    )


class Leviathan(TitanClass):
    name = Prop("Leviathan Class")
    encounter_chance = Prop(0.5)
    species_class = Prop("Juvenile")
    health_point = PropWithMax(200, 200)
    strength = PropWithMax(5, 25)
    intellect = PropWithMax(7, 12)
