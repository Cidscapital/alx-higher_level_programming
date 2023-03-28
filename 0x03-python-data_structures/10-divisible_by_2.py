#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    result = []
    for i in range(length):
        if my_list[i] == 0:
            result.append(True)
        elif my_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
