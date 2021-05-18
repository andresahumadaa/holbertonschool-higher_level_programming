#!/usr/bin/python3
'''safe_print_list'''


def safe_print_integer(value):
    '''prints x elements of a list'''
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
