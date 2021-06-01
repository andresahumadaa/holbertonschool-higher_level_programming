#!/usr/bin/python3
'Write'


def write_file(filename="", text=""):
    'writes a string to a text file (UTF8) and returns'
    with open(filename, mode="w", encoding="utf-8") as w:
        w.write(text)
        return len(text)
