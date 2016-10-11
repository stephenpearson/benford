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

"""Test cases for Benford."""

from testtools import TestCase

import benford.main as bm


class TestBenford(TestCase):
    """Test case docstring."""

    def test_generate_numbers_empty(self):
        """Minimal parameters for generate_numbers."""
        self.assertEqual([], bm.generate_numbers(0, 0))
        self.assertEqual([1], bm.generate_numbers(1, 1))

    def test_generate_numbers_different(self):
        """Do the values returned look more or less random."""
        numbers = bm.generate_numbers(100, 100)
        self.assertEqual(100, len(numbers))
        self.assertTrue(len(set(numbers)) > 1)

    def test_generate_numbers_invalid_range(self):
        """Invalid number range should return an error."""
        self.assertRaises(ValueError, bm.generate_numbers, 10, -1)

    def test_get_first_digits_empty(self):
        """Minimal parameters for get_first_digits."""
        self.assertEqual([], bm.get_first_digits([]))
        self.assertEqual([1], bm.get_first_digits([1]))

    def test_get_first_digits(self):
        """First digit should be returned correctly."""
        numbers = [1, 234, 345]
        self.assertEqual([1, 2, 3], bm.get_first_digits(numbers))

    def test_get_distribution(self):
        """Distribution or count of numbers in list."""
        self.assertEqual(([0] * 10, 0), bm.get_distribution([]))

        nums = [1, 2, 4, 3, 1, 2, 1, 2, 5, 3]
        dist = ([0, 3, 3, 2, 1, 1, 0, 0, 0, 0], 3)
        self.assertEqual(dist, bm.get_distribution(nums))

    def test_get_histogram(self):
        """Return a histogram as a multi-line string."""
        data = [1, 1, 1, 2, 2, 3]
        result = bm.get_histogram(data)
        self.assertRegex(result, r'1 : \*.+')
        self.assertRegex(result, r'2 : \*.+')
        self.assertRegex(result, r'3 : \*.+')
        self.assertRegex(result, r'4 : \n')
