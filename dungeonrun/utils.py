import importlib
import os
import random
import time
from typing import Union


def animate(string_: str, delay: float = 0.014) -> None:
    """
    Adds delay before printing each character to "animate" it.
    """
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


def import_from_app(app_name: str, path: str):
    """Handles importing module and class."""

    *file_directory, class_name = path.split(".")

    return getattr(
        importlib.import_module(f"app.{app_name}.{'.'.join(file_directory)}"),
        class_name,
    )


def clear_stdout() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def join_iter(
    iterable: Union[list, tuple],
    separator: str = " :: ",
    str_method: str = "upper",
) -> str:
    return separator.join(
        getattr(str(item), str_method)() for item in iterable
    )
