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
# prime1.py
# Python specification of the class prime1
#
# Created on:      25-Nov-2019
# Original author: mmaylat
#-------------------------------------------------------------------------------
"""Prints 'primeness' information about the numbers in the specified range

Usage Examples:

    >>> prime1()
    2 is a prime number
    3 is a prime number
    4 equals 2 * 2

    >>> prime1(4, 10)
    4 equals 2 * 2
    5 is a prime number
    6 equals 2 * 3
    7 is a prime number
    8 equals 2 * 4
    9 equals 3 * 3
    10 equals 2 * 5

"""
# Your Imports Here:
from __future__ import print_function, division, absolute_import, unicode_literals

def prime1(nFirst=2, nLast=4):
    """Prints 'primeness' information about the numbers in the specified range

    :param nFirst: The first number to account for, default is 2.
    :param nLast: The last number to account for, default is 4
    """
    for n in range(nFirst, nLast+1):
        for x in range(2, n):
            if n % x == 0:
                print('{} equals {:} * {:}'.format(n, x, int(n/x)))
                break
            else:
                continue
        else:
            print(n, 'is a prime number')

if __name__ == '__main__':  # pragma: no cover
    from doctest import testmod
    print(testmod())
