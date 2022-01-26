import importlib
import inspect
import os

from dungeonrun.dungeonrun import DungeonRun

if __name__ == "__main__":
    folders = os.listdir("./pack")
    installed_pack = {}

    for folder in folders:
        try:
            module = importlib.import_module(f"pack.{folder}.app")
        except ModuleNotFoundError:
            pass
        else:
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if DungeonRun in cls.__mro__ and cls is not DungeonRun:
                    installed_pack[folder] = cls

    print("List of installed pack:")
    for index, pack in enumerate(installed_pack):
        print(f"{index + 1}. {pack}")

    while True:
        try:
            chosen_pack = input("\nDesired pack: ")
            installed_pack[chosen_pack]().run()
        except KeyError:
            print("Pack not found")
            continue
