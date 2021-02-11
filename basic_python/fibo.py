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
# fibo.py
#
# Created on:      25-Feb-2019
# Original author: mmaylat
#-------------------------------------------------------------------------------
"""Fibonacci sequence Implementation - using a simple function

Write Fibonacci sequence up to (and not including) the provided number.

The main purpose of this module is the illustration of various import forms.

For example, you can import this module as-is and access its underlying
function:

    >>> import basic_python.fibo
    >>> basic_python.fibo.fib(100)      # doctest: +NORMALIZE_WHITESPACE
    1 1 2 3 5 8 13 21 34 55 89

Alternatively you can use a "from - import" statement for a more compact syntax:

    >>> from basic_python import fibo
    >>> fibo.fib(50)                    # doctest: +NORMALIZE_WHITESPACE
    1 1 2 3 5 8 13 21 34

Or you could use 'on the fly rename' statement like so:

    >>> from basic_python.fibo import fib as fibonacci
    >>> fibonacci(30)                   # doctest: +NORMALIZE_WHITESPACE
    1 1 2 3 5 8 13 21

You can import all 'public' members of a module without explicitly naming them,
however this is strongly discouraged as it can introduce unpredictable
consequences:

    >>> from basic_python.fibo import *
"""
# Your Imports Here:
from __future__ import print_function, division, absolute_import, unicode_literals

def fib(n):
    """Write Fibonacci sequence up to and not including n

    Usage example:

        >>> fib(3)                         # doctest: +NORMALIZE_WHITESPACE
        1 1 2
        >>> fib(4)                         # doctest: +NORMALIZE_WHITESPACE
        1 1 2 3
        >>> fib(5)                         # doctest: +NORMALIZE_WHITESPACE
        1 1 2 3
        >>> fib(6)                         # doctest: +NORMALIZE_WHITESPACE
        1 1 2 3 5
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    print()     # Finalize with a new line

if __name__ == '__main__':  # pragma: no cover
    fib(5)     # self-test code
