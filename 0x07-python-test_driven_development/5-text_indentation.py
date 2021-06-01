#!/usr/bin/python3
''' Text indentation '''


def text_indentation(text):
    ''' prints a text with 2 new lines after each of these characters: ., ? and : '''
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]))
            print()
            if (i + 1) < len(text):
                if text[i + 1] == ' ':
                    i += 1
        i += 1
