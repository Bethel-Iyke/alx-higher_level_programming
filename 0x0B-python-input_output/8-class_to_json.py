#!/usr/bin/python3
"""
contains the "class_to json" function
"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
