#!/usr/bin/python3
"""This function returns an object PYTHON data structure by JSON"""

import json


def from_json_string(my_str):
    """to decoad the object again if its in binary"""
    return json.loads(my_str)
