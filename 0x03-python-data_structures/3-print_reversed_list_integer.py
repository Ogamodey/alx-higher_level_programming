#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list = reversed(my_list)

    for item in reversed(my_list):
        print("{:d}".format(item))
