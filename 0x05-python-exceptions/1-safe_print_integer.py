#!/usr/bin/python3
'''safe_print_list'''


def safe_print_integer(value):
    '''prints x elements of a list'''
    try:
        number = int(value)
        print(number)
        return True
    except:
        return False
