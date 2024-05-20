#!/usr/bin/python3
def max_integer(list=[]):
    """Function to find and return the maximum integer in a list of integers.
       If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    max_val = list[0]
    for num in list:
        if num > max_val:
            max_val = num
    return max_val
