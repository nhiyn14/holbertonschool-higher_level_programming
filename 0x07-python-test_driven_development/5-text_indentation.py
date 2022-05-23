#!/usr/bin/python3
"""Module to add new line in text
"""


def text_indentation(text):
    """prints a text with 2 new lines after . and ? and :
    Returns: text with added new line
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    alert = 0

    for char in text:
        if alert == 0:
            if char == " ":
                continue
            else:
                alert = 1
        if alert == 1:
            if char == "?" or char == "." or char == ":":
                print(char)
                print()
                alert = 0
            else:
                print(char, end="")
