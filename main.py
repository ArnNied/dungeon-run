import sys
from importlib import import_module
from os import system

from dungeonrun import config as cf
from dungeonrun.actor.base import BaseActor

if __name__ == "__main__":
    try:
        pack_config_path = "pack.{pack_name}.config".format(
            pack_name=cf.PACK_NAME
        )
        pack_config = import_module(pack_config_path)
        (
            SECTOR_BEGIN_FILE,
            SECTOR_BEGIN_CLASS,
        ) = pack_config.SECTOR_BEGIN.split(".")
    except (AttributeError, ValueError):
        print(
            """
        Pack config error: Make sure 'SECTOR_BEGIN' in pack/{pack_name}/config.py is configured correctly
        Example: 'FILE_NAME.CLASS_NAME'
        """.format(
                pack_name=cf.PACK_NAME
            )
        )
        sys.exit(1)
    except ModuleNotFoundError:
        print(
            """
        Pack error:
        Make sure the pack is installed correctly and 'PACK_NAME' correctly configured in dungeonrun/config.py
        PACK_NAME: {pack_name}
        """.format(
                pack_name=cf.PACK_NAME
            )
        )
        sys.exit(1)

    system("cls")
    player = BaseActor()

    sector_path = "pack.{pack_name}.sector.{sector_begin}".format(
        pack_name=cf.PACK_NAME, sector_begin=SECTOR_BEGIN_FILE
    )
    sector = getattr(import_module(sector_path), SECTOR_BEGIN_CLASS)

    while True:
        system("cls")
        sector = sector(player).execute()
