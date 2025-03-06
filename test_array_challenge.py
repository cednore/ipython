"""
Test file for the Array Manipulation Challenge
"""

import unittest
from array_challenge import (
    my_map,
    my_filter,
    my_reduce,
    flatten_array,
    group_by,
    chain_operations,
)


class TestArrayChallenge(unittest.TestCase):

    def test_my_map(self):
        self.assertEqual(my_map([1, 2, 3], lambda x: x * 2), [2, 4, 6])
        self.assertEqual(
            my_map(["hello", "world"], lambda x: x.upper()), ["HELLO", "WORLD"]
        )
        self.assertEqual(my_map([], lambda x: x * 2), [])

    def test_my_filter(self):
        self.assertEqual(my_filter([1, 2, 3, 4], lambda x: x % 2 == 0), [2, 4])
        self.assertEqual(
            my_filter(["apple", "banana", "cherry"], lambda x: len(x) > 5),
            ["banana", "cherry"],
        )
        self.assertEqual(my_filter([], lambda x: x > 0), [])

    def test_my_reduce(self):
        self.assertEqual(my_reduce([1, 2, 3], lambda acc, curr: acc + curr, 0), 6)
        self.assertEqual(
            my_reduce(["a", "b", "c"], lambda acc, curr: acc + curr, ""), "abc"
        )
        self.assertEqual(my_reduce([], lambda acc, curr: acc + curr, 10), 10)

        # Test with no initial value
        self.assertEqual(my_reduce([1, 2, 3, 4], lambda acc, curr: acc + curr), 10)

        # Test with empty array and no initial value
        with self.assertRaises(ValueError):
            my_reduce([], lambda acc, curr: acc + curr)

    def test_flatten_array(self):
        self.assertEqual(flatten_array([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten_array([1, 2, 3]), [1, 2, 3])
        self.assertEqual(flatten_array([]), [])
        self.assertEqual(flatten_array([[], []]), [])

    def test_group_by(self):
        self.assertEqual(
            group_by([1, 2, 3, 4, 5], lambda x: "even" if x % 2 == 0 else "odd"),
            {"even": [2, 4], "odd": [1, 3, 5]},
        )
        self.assertEqual(
            group_by(["apple", "banana", "cherry", "date"], lambda x: len(x)),
            {5: ["apple"], 6: ["banana", "cherry"], 4: ["date"]},
        )
        self.assertEqual(group_by([], lambda x: x), {})

    def test_chain_operations(self):
        self.assertEqual(chain_operations([1, 2, 3, 4]), 20)  # 2² + 4² = 4 + 16 = 20
        self.assertEqual(chain_operations([1, 3, 5, 7]), 0)  # No even numbers
        self.assertEqual(
            chain_operations([2, 4, 6]), 56
        )  # 2² + 4² + 6² = 4 + 16 + 36 = 56
        self.assertEqual(chain_operations([]), 0)  # Empty array


if __name__ == "__main__":
    print("Running tests for the Array Manipulation Challenge...")
    unittest.main()
