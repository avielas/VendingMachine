#!/usr/bin/env python2.7.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

def verbing(s):
    """D. Apply a verbing strategy on a string

    Given a string, if its length is at least 3,
    add 'ing' to its end.
    Unless it already ends in 'ing', in which case
    add 'ly' instead.
    If the string length is less than 3, leave it unchanged.
    Return the resulting string.

    Usage example:

        >>> verbing('hail')
        'hailing'
        >>> verbing('swimming')
        'swimmingly'
        >>> verbing('do')
        'do'

    :param s: string to be 'verbed'
    :return: the resulting string
    """
    # +++your code here+++
    return


def not_bad(s):
    """E. Convert a "not * bad" phrase to "good"

    Given a string, find the first appearance of the
    substring 'not' and 'bad'. If the 'bad' follows
    the 'not', replace the whole 'not'...'bad' substring
    with 'good'.
    Return the resulting string.
    So 'This dinner is not that bad!' yields:
    This dinner is good!

    Usage example:

        >>> not_bad('This movie is not so bad')
        'This movie is good'
        >>> not_bad('This dinner is not that bad!')
        'This dinner is good!'
        >>> not_bad('This tea is not hot')
        'This tea is not hot'
        >>> not_bad("It's bad yet not")
        "It's bad yet not"

    :param s: string to be simplified
    :return: the resulting string
    """
    # +++your code here+++
    return


def front_back(a, b):
    """F. Apply a 'mixed split' of two string

    Consider dividing a string into two halves.
    If the length is even, the front and back halves are the same length.
    If the length is odd, we'll say that the extra char goes in the front half.
    e.g. 'abcde', the front half is 'abc', the back half 'de'.
    Given 2 strings, a and b, return a string of the form::

      a-front + b-front + a-back + b-back

    Usage example:

        >>> front_back('abcd', 'xy')
        'abxcdy'
        >>> front_back('abcde', 'xyz')
        'abcxydez'
        >>> front_back('Kitten', 'Donut')
        'KitDontenut'

    :param a: a string to be mixed
    :param b: another string o be mixed
    :return: The resulting mixed string
    """
    # +++your code here+++
    return


if __name__ == '__main__':  # pragma: no cover
    # Provided a standard method to check if each result is correct or not
    # from a command line.
    # Use PyCharm to test each individual function and more!!!
    from doctest import testmod
    print(testmod())
