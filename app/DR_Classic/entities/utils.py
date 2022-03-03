from dungeonrun.prop import PropWithMax


class RandomizedNumber(PropWithMax):
    def __str__(self):
        return f"{self.value} - {self.max_value}"
