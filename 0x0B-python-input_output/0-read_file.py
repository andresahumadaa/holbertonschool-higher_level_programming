#!/usr/bin/python3
'Read file'


def read_file(filename=""):
    'reads a text'
    with open(filename, encoding="utf-8") as r:
        print(r.read(), end="")
