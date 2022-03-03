import importlib
import inspect
import os

from dungeonrun.dungeonrun import DungeonRun

if __name__ == "__main__":
    folders = os.listdir("./app")
    installed_app = {}

    for folder in folders:
        try:
            module = importlib.import_module(f"app.{folder}.app")
        except ModuleNotFoundError:
            pass
        else:
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if DungeonRun in cls.__mro__ and cls is not DungeonRun:
                    installed_app[folder] = cls

    print("List of installed app:")
    for index, app in enumerate(installed_app):
        print(f"{index + 1}. {app}")

    while True:
        chosen_app = input("\nChoose an app: ")

        if chosen_app not in installed_app:
            print("App not found")
            continue
        else:
            break
    installed_app[chosen_app]().run()
