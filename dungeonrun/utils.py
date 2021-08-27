import os
import sys
import inspect

from random import random, uniform
from importlib import import_module
from inspect import getmro

from dungeonrun import config

def rng() -> float:
    """Main rng function"""

    return random()

def convert_to_keys(string: str) -> str:
    """
    This will replace space in string with underscore for dictionary key use
    
    'This Is An Example' -> 'this_is_an_example'
    """

    return '_'.join(string.lower().split(' '))

def convert_to_readable(string: str) -> str:
    """
    This will replace underscore in string with space for user to read

    'this_is_an_example' -> 'This Is An Example' 
    """

    return ' '.join(string.split('_')).title()

def import_from_pack(path: str):
    """Handles importing module and class"""

    *file_directory, class_name = path.split('.')
    
    return getattr(import_module(f"pack.{config.PACK_NAME}.{'.'.join(file_directory)}"), class_name)

# def get_parents(class_):
#     """
#     Function to use when 'isinstance()' cannot be used.
    
#     Return name of all parent classes from 'class_'.
#     """

#     return [parent.__name__ for parent in getmro(class_)]