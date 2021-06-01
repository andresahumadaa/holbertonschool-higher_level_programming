#!/usr/bin/python3
'Save Object'
import json


def save_to_json_file(my_obj, filename):
    'writes an Object to a text filen'
    with open(filename, mode="w", encoding="utf-8") as s:
        json.dump(my_obj, s)
