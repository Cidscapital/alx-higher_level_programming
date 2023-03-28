#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_n = list(map(lambda x: replace if x == search else x, my_list))
    return (list_n)
