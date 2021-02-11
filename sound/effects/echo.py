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
# echo.py
# Python specification of the class echo
#
# Created on:      25-Feb-2019
# Original author: mmaylat
#-------------------------------------------------------------------------------
"""Echo Implementation of illustrating package structuring:

To declare folder as package, it must have __init__.py file::

    sound/                     # top-level package
          __init__.py          # initialize the sound package
          effects/             # sub-package for sound effects
                  __init__.py  # initialize the effects package
                  echo.py      # module

Import syntax examples:

    >>> import sound.effects.echo
    >>> sound.effects.echo.apply()
    WOO WOOO WOOOO WOOOOO

    >>> from sound.effects import echo
    >>> echo.apply(7)
    WOO WOOO WOOOO WOOOOO WOOOOOO WOOOOOOO WOOOOOOOO

    >>> from sound.effects.echo import apply
    >>> apply(9)
    WOO WOOO WOOOO WOOOOO WOOOOOO WOOOOOOO WOOOOOOOO WOOOOOOOOO WOOOOOOOOOO
"""

def apply(reflections=4):
    print(' '.join('W'+'O'*(2+i) for i in range(reflections)))
