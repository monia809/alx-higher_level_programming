#!/usr/bin/python3
"""This module definefunction."""


def append_write(filename="", text=""):
    """Appends a sTF8 text file
    """
    with open(filename, "a", encoding="u-8") as f:
        return f.write(text)
