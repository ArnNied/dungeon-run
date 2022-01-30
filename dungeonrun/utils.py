import importlib
import os
import random
import time
from typing import Union


def animate(string_: str, delay: float = 0.014) -> None:
    for char in string_:
        print(char, end="", flush=True)
        time.sleep(delay)


def rng(val: float = None) -> Union[bool, float]:
    """Will return bool after evaluating `random() <= val` or return float from `random()`"""

    if val is not None:
        return random.random() <= val

    return random.random()


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


def import_from_pack(pack_name: str, path: str):
    """Handles importing module and class."""

    *file_directory, class_name = path.split(".")

    return getattr(
        importlib.import_module(
            f"pack.{pack_name}.{'.'.join(file_directory)}"
        ),
        class_name,
    )


def clear_stdout():
    os.system("cls" if os.name == "nt" else "clear")
