#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstration of Benford's Law.

Plots the results of a sequence of lambda functions applied to a set of
random data. Shows the relative frequencies of every most significant digit
to illustrate that the resulting distribution is not random, as might be
expected.

See https://en.wikipedia.org/wiki/Benford's_law for details.
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from random import randint


def generate_numbers(qty, maxval):
    """Generate and return a list of random numbers.

    This function generates and returns a list of <qty> numbers with a value
    between 1 and <maxval>.  This will be used as the raw input to be fed into
    the sequence of lambda expressions later.

    :param qty: the size of the list.
    :param maxval: the maximum value of each element in the list.
    :returns: list -- a list of random numbers.
    """
    numbers = []
    for i in range(qty):
        numbers.append(randint(1, maxval))
    return numbers


def get_first_digits(numbers):
    """Extract the first digits from a list of numbers.

    :param numbers: a list of numbers
    :returns: list -- a list representing the first digit of each number in the
                      input list.
    """
    def fd(x):
        return int(str(x)[0])
    return map(fd, numbers)


def get_distribution(fnumbers):
    """Return the number of occurances of each number in a list.

    Iterate over a list of numbers and return the number of times each unique
    number occurs.  This result can be used to display a histogram of relative
    occurances.

    :param fnumbers: the list of numbers
    :returns: tuple -- the number of occurances for each digit, and a max
                       occurance value.  This latter value is used to scale
                       the histogram.
    """
    def count_num(value):
        return len([i for i in fnumbers if i == value])

    result = [count_num(i) for i in range(0, 10)]
    return (result, max(result))


def get_histogram(data, width=70):
    """Output the relative frequencies of a list of numbers as a histogram.

    :param data: list of numbers
    """
    result = ""
    (distrib, max_count) = get_distribution(data)
    div = max_count / width
    for i in range(1, 10):
        count = distrib[i]
        result += ("{0} : {1}\n".format(i, "*" * int(count / div)))
    return result


def main():
    """CLI entry point.

    A list of numbers is generated, then a series of lambda functions are
    applied to the list in turn, then finally the size of the set of first
    digits of each number in the list are computed and displayed as a
    histogram.
    """
    numbers = generate_numbers(100000, 10000)

    # Map a series of functions to the set
    fns = "* 8, ** 5, + 50, * 7, - 17"
    for f in fns.split(", "):
        numbers = map(eval("lambda x: x %s" % f), numbers)

    fnumbers = get_first_digits(numbers)
    print(get_histogram(fnumbers))


if __name__ == "__main__":
    main()    # pragma: no cover
