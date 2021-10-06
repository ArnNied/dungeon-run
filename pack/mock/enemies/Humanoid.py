from dungeonrun.actor.base import BaseActor

class Elvish(BaseActor):
    name = "Elvish Class"
    encounter_chance = 0.8

class Orc(BaseActor):
    name = "Orc Class"
    encounter_chance = 0.7

class Human(BaseActor):
    name = "Human Class"
    encounter_chance = 0.5