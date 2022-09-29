#!/usr/bin/python3
"""this function returns the JSON representation of an object"""


def to_json_string(my_obj):
    """Returns JSON"""
    import json
    return json.dumps(my_obj)
