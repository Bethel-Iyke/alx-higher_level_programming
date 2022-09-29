#!/usr/bin/python3
"""
fucnction that reads a text file
"""


def read_file(filename=""):
    """reads a text file (utf8) and printd it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
