#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Return peak in a list of unsorted integers"""

    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    peak = list_of_integers[low]

    if low > 0 and peak < list_of_integers[low - 1]:
        return None

    return peak
