#!/usr/bin/python3

"""
Contains the "load_from_json_file
"""

import json


def load_from_json_file(filename):
    """creates an object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
