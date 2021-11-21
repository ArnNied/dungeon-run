import sys
from importlib import import_module
from os import system

from dungeonrun import config as cf
from dungeonrun.actor.base import BaseActor

if __name__ == "__main__":
    try:
        pack_config_path = f"pack.{cf.PACK_NAME}.config"
    except (AttributeError, ValueError):
        print(
            f"""
        Config error:
        Make sure 'PACK_NAME' is configured in dungeonrun/config.py
        """
        )
        sys.exit(1)

    try:
        pack_config = import_module(pack_config_path)

        (
            SECTOR_BEGIN_FILE,
            SECTOR_BEGIN_CLASS,
        ) = pack_config.SECTOR_BEGIN.split(".")
    except AttributeError:
        print(
            f"""
        Pack config error:
        Make sure 'SECTOR_BEGIN' is configured in pack/{cf.PACK_NAME}/config.py
        PACK_NAME: {cf.PACK_NAME}
        """
        )
        sys.exit(1)
    except ValueError:
        print(
            f"""
        Pack import error:
        Make sure 'SECTOR_BEGIN' is configured correctly in dungeonrun/config.py. Ex: 'FILE_NAME.CLASS_NAME'
        PACK_NAME: {cf.PACK_NAME}
        SECTOR_BEGIN: {pack_config.SECTOR_BEGIN}
        """
        )
        sys.exit(1)
    except ModuleNotFoundError:
        print(
            f"""
        Pack not found:
        Make sure the pack is installed correctly and 'PACK_NAME' correctly configured in dungeonrun/config.py
        PACK_NAME: {cf.PACK_NAME}
        """
        )
        sys.exit(1)

    system("cls")
    player = BaseActor()

    sector_path = f"pack.{cf.PACK_NAME}.sector.{SECTOR_BEGIN_FILE}"
    sector = getattr(import_module(sector_path), SECTOR_BEGIN_CLASS)

    while True:
        system("cls")
        sector = sector(player).execute()
