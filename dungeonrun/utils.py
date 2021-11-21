import os
import sys
import inspect

from random import random, uniform
from importlib import import_module
from inspect import getmro
from time import sleep

from dungeonrun import config


def rng() -> float:
    """Main rng function"""

    return random()


def timed(text, before=0, after=0.75):
    """
    Add a pause before and/or after a text.

    before: Mainly used for notification such as level up

    after: Mainly used for dialogue
    """

    sleep(before)
    print(text)
    sleep(after)


def convert_to_keys(string: str) -> str:
    """
    This will replace space in string with underscore for dictionary key use

    'This Is An Example' -> 'this_is_an_example'
    """

    return "_".join(string.lower().split(" "))


def convert_to_readable(string: str) -> str:
    """
    This will replace underscore in string with space for user to read

    'this_is_an_example' -> 'This Is An Example'
    """

    return " ".join(string.split("_")).title()


def import_from_pack(path: str):
    """Handles importing module and class"""

    *file_directory, class_name = path.split(".")

    return getattr(
        import_module(f"pack.{config.PACK_NAME}.{'.'.join(file_directory)}"), class_name
    )
