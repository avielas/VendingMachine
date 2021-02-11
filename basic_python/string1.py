#!/usr/intel/bin/python2.6.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


def donuts(count):
    """A. Report number of donuts

    Given an int count of a number of donuts, return a string
    of the form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word 'many'
    instead of the actual count.
    So donuts(5) returns 'Number of donuts: 5'
    and donuts(23) returns 'Number of donuts: many'

    Usage example:

        >>> donuts(4)
        'Number of donuts: 4'

        >>> donuts(9)
        'Number of donuts: 9'
        >>> donuts(10)
        'Number of donuts: many'
        >>> donuts(99)
        'Number of donuts: many'

    :param count: The number of donuts
    :return: String message reporting on the number of donuts
    """
    # +++your code here+++
    return


def both_ends(s):
    """B. Return only both ends of a string

    Given a string s, return a string made of the first 2
    and the last 2 chars of the original string,
    so 'spring' yields 'spng'. However, if the string length
    is less than 2, return instead the empty string.

    Usage example:

        >>> both_ends('spring')
        'spng'
        >>> both_ends('Hello')
        'Helo'
        >>> both_ends('a')
        ''
        >>> both_ends('xyz')
        'xyyz'

    :param s: The given string
    :return: The output string consisting only on both ends of the original
    """
    # +++your code here+++
    return


def fix_start(s):
    """C. Hide the start character in the rest of a string

    Given a string s, return a string
    where all occurrences of its first char have
    been changed to '*', except do not change
    the first char itself.
    e.g. 'babble' yields 'ba**le'
    Assume that the string is length 1 or more.

    Usage example:

        >>> fix_start('babble')
        'ba**le'
        >>> fix_start('aardvark')
        'a*rdv*rk'
        >>> fix_start('google')
        'goo*le'
        >>> fix_start('donut')
        'donut'

    :param s: The given string
    :return: Modified string
    """
    # +++your code here+++
    # Hint: s.replace(stra, strb) returns a version of string s
    # where all instances of stra have been replaced by strb.
    return


def mix_up(a, b):
    """D. MixUp two strings

    Given strings a and b, return a single string with a and b separated
    by a space '<a> <b>', except swap the first 2 chars of each string.
    e.g.::

      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'

    Assume a and b are length 2 or more.

    Usage example:

        >>> mix_up('mix', 'pod')
        'pox mid'
        >>> mix_up('dog', 'dinner')
        'dig donner'
        >>> mix_up('gnash', 'sport')
        'spash gnort'
        >>> mix_up('pezzy', 'firm')
        'fizzy perm'

    :param a: a string
    :param b: another string
    :return: The 'mixup'
    """
    # +++your code here+++
    return


if __name__ == '__main__':  # pragma: no cover
    # Provided a standard method to check if each result is correct or not
    # from a command line.
    # Use PyCharm to test each individual function and more!!!
    from doctest import testmod
    print(testmod())
