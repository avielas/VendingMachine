#-------------------------------------------------------------------------------
# INTEL CONFIDENTIAL
# Copyright 2019 Intel Corporation All Rights Reserved.
# The source code contained or described herein and all documents related
# to the source code ("Material") are owned by Intel Corporation or its
# suppliers or licensors. Title to the Material remains with Intel Corp-
# oration or its suppliers and licensors. The Material contains trade
# secrets and proprietary and confidential information of Intel Corpor-
# ation or its suppliers and licensors. The Material is protected by world-
# wide copyright and trade secret laws and treaty provisions. No part of
# the Material may be used, copied, reproduced, modified, published,
# uploaded, posted, transmitted, distributed, or disclosed in any way
# without Intel's prior express written permission.
# No license under any patent, copyright, trade secret or other intellect-
# ual property right is granted to or conferred upon you by disclosure or
# delivery of the Materials, either expressly, by implication, inducement,
# estoppel or otherwise. Any license under such intellectual property
# rights must be express and approved by Intel in writing.
#
# Stacks.py
# Python specification of the class Stacks
#
# Created on:      26-Feb-2019
# Original author: mmaylat
#-------------------------------------------------------------------------------
"""Stack Implementations targeted for illustrating the usage of a 'class'.
"""
# Your Imports Here:
from __future__ import print_function


class Stack(object):
    """Basic Stack Implementation

    You can create (instantiate) a `Stack`, then use the `push`/`pop` operations
    on it:

        >>> s1 = Stack()
        >>> s1.push(3)
        >>> s1.push(4)
        >>> s1.push(5)

    You can have multiple instances, each with its self-identity:

        >>> s2 = Stack()
        >>> s2.push(7)
        >>> s2.push(8)

    A `Stack` has a dedicated representation function:

        >>> s1
        Stack< 5 | 4 | 3 >
        >>> s1.pop()
        5
        >>> s1
        Stack< 4 | 3 >

        >>> s2
        Stack< 8 | 7 >

        >>> s1.pop()
        4
        >>> s2.pop()
        8

    At any time you can query the size of the stack:

        >>> len(s1)
        1
        >>> s1.push(7); len(s1)
        2
    """
    def __init__(self):
        self._items = []
    def push(self, x):
        """Add item to the top of stack"""
        self._items.append(x)
    def pop(self):
        """Remove item from the top of stack and return it"""
        return self._items.pop()

    # Define custom behavior
    #------------------------------
    def __nonzero__(self):
        """return true if not empty
        """
        return len(self._items) != 0

    def __len__(self):
        """Return the number of items in the stack"""
        return len(self._items)

    def __iadd__(self, other):
        """Push all content from the other stack ("+=" operator)
        """
        for item in other._items:
            self.push(item)
        return self

    def __repr__(self):
        """Useful representation function"""
        return '{name}< {items} >'.format(
            name = self.__class__.__name__,
            items = ' | '.join(str(v) for v in reversed(self._items)),
        )
# end class Stack


class LimitedStack(Stack):
    """Stack with a size limit

    Usage example:

    >>> s1 = Stack()
    >>> s1.push(1)
    >>> s1.push(2)

    >>> s2 = LimitedStack(5)
    >>> s2 += s1
    >>> s2 += s1
    >>> s2
    LimitedStack< 2 | 1 | 2 | 1 >
    >>> s2 += s1
    Traceback (most recent call last):
        ...
    AssertionError: Size limit (5) reach

    >>> s2
    LimitedStack< 1 | 2 | 1 | 2 | 1 >
    """
    def __init__(self, limit):
        super(LimitedStack, self).__init__()  # base class initialize method
        self._limit = limit

    def push(self, x):
        """Add item to the top of stack"""
        assert len(self._items) < self._limit, 'Size limit ({}) reach'.format(self._limit)
        super(LimitedStack, self).push(x)     # base class method call
# end class LimitedStack


if __name__ == '__main__':  # pragma: no cover
    from doctest import testmod
    print(testmod())
