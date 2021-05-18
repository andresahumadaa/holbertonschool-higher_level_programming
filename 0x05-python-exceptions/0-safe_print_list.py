#!/usr/bin/python3
'''safe_print_list'''


def safe_print_list(my_list=[], x=0):
    '''prints x elements of a list'''
    a = 0
    b = 0
    while a < x:
        try:
            print("{}".format(my_list[a]), end="")
            a += 1
            b += 1
        except:
            break
    print()
    return b
