#!/usr/intel/bin/python2.6.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. Implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

Usage example:

    >>> import os
    >>> curr_dir = os.path.dirname(__file__)
    >>> source_file = (os.path.join(curr_dir, 'wordcount_input.txt'))

    >>> print_words(source_file)
    -- 1
    are 3
    at 1
    be 3
    but 1
    coach 1
    football 1
    least 1
    need 1
    not 3
    should 1
    to 2
    used 1
    we 6
    what 3

2. Implement a print_top(filename) which is similar
to print_words() but which prints just the top 5 most common words sorted
so the most common word is first, then the next most common, and so on.

Usage example:

    >>> print_top(source_file)
    we 6
    are 3
    be 3
    not 3
    what 3

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""
from __future__ import print_function
import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


if __name__ == '__main__':  # pragma: no cover
    # Provided a standard method to check if each result is correct or not
    # from a command line.
    # Use PyCharm to test each individual function and more!!!
    from doctest import testmod
    print(testmod())
