from dungeonrun.encounter import Encounter


class MyEncounter(Encounter):
    def execute(self):
        print(self.opfor.stringify_prop())
        print("custom execute")
