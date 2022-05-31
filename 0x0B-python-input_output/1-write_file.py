#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
returns the number of characters written
"""


def write_file(filename="", text=""):
    """write str to text file and return num of char"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
