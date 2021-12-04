from importlib import import_module
from random import random
from time import sleep
from typing import Union

from dungeonrun import config


def animate(string_):
    for char in string_:
        print(char, end="", flush=True)
        sleep(0.015)


def rng(val: float = None) -> Union[bool, float]:
    """Will return bool after evaluating `random() <= val` or return float from `random()`"""

    if val is not None:
        return random() <= val

    return random()


def convert_to_keys(string: str) -> str:
    """
    This will replace space in string with underscore for dictionary key use.

    'This Is An Example' -> 'this_is_an_example'
    """

    return "_".join(string.lower().split(" "))


def convert_to_readable(string: str) -> str:
    """
    This will replace underscore in string with space for user to read.

    'this_is_an_example' -> 'This Is An Example'
    """

    return " ".join(string.split("_")).title()


def import_from_pack(path: str):
    """Handles importing module and class."""

    *file_directory, class_name = path.split(".")

    return getattr(
        import_module(f"pack.{config.PACK_NAME}.{'.'.join(file_directory)}"),
        class_name,
    )
