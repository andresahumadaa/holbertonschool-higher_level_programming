#!/usr/bin/python3
'Append to a file'


def append_write(filename="", text=""):
    'appends a string at the end of a text file'
    with open(filename, mode="a", encoding="utf-8") as a:
        a.write(text)
        return(len(text))
