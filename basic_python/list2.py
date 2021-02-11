#!/usr/bin/env python2.7.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

def remove_adjacent(nums):
    """D. Remove equal adjacent values

    Given a list of numbers, return a list where
    all adjacent == elements have been reduced to a single element,
    so [1, 2, 2, 3] returns [1, 2, 3].

    Usage example:

        >>> remove_adjacent([1, 2, 2, 3])
        [1, 2, 3]
        >>> remove_adjacent([2, 2, 3, 3, 3])
        [2, 3]
        >>> remove_adjacent([])
        []

    You may create a new list or
    modify the passed in list.

    :param nums: a list of numbers
    :return: The list with removed adjacent values that are equal
    """
    # +++your code here+++
    return


def linear_merge(list1, list2):
    """ E. Merge sorted list in linear time

    Given two lists sorted in increasing order, create and return a merged
    list of all the elements in sorted order. You may modify the passed in lists.
    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.

    Usage example:

        >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
        ['aa', 'bb', 'cc', 'xx', 'zz']
        >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
        ['aa', 'bb', 'cc', 'xx', 'zz']
        >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
        ['aa', 'aa', 'aa', 'bb', 'bb']

    :param list1: A sorted list
    :param list2: Another sorted list
    :return: Sorted merge of the two input lists
    """
    # +++your code here+++
    return


if __name__ == '__main__':  # pragma: no cover
    # Provided a standard method to check if each result is correct or not
    # from a command line.
    # Use PyCharm to test each individual function and more!!!
    from doctest import testmod
    print(testmod())