#!/usr/intel/bin/python2.6.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

def match_ends(words):
    """A. Match Ends - count the number of words with matched ends

    Given a list of strings, return the count of the number of
    strings where the string length is 2 or more and the first
    and last chars of the string are the same.
    Note: python does not have a ++ operator, but += works.

    Usage example:

        >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
        3
        >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
        2
        >>> match_ends(['aaa', 'be', 'abc', 'hello'])
        1

    :param words: A list of words
    :return: The number of words with 'Matched Ends'
    """
    # +++your code here+++
    return


def front_x(words):
    """B. Front 'x' - sort with precedence to beginning with 'x'

    Given a list of strings, return a list with the strings
    in sorted order, except group all the strings that begin with 'x' first.

    Usage example:

        >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
        >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
        >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
        >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    Hint: this can be done by making 2 lists and sorting each of them
    before combining them.

    :param words: A list of words
    :return: 'words' sorted with precedence to those that begin with 'x'
    """
    # +++your code here+++
    return

def sort_last(list_of_tuples):
    """C. Sort Last - sort a list of list_of_tuples by the list_of_tuples' last element

    Given a list of non-empty list_of_tuples, return a list sorted in increasing
    order by the last element in each tuple.

    Usage example:

        >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
        >>> sort_last([(1, 3), (3, 2), (2, 1)])
        [(2, 1), (3, 2), (1, 3)]
        >>> sort_last([(2, 3), (1, 2), (3, 1)])
        [(3, 1), (1, 2), (2, 3)]
        >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

    Hint: use a custom key= function to extract the last element form each tuple.

    :param list_of_tuples: A list of tuples
    :return: The list of tuples sorted by the last element of each tuple
    """
    # +++your code here+++
    return


if __name__ == '__main__':  # pragma: no cover
    # Provided a standard method to check if each result is correct or not
    # from a command line.
    # Use PyCharm to test each individual function and more!!!
    from doctest import testmod
    print(testmod())
