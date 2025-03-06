"""
Test file for the Advanced Array Manipulation Challenge
"""

import unittest
from array_challenge_advanced_solution import compose, pipe, memoize, zip_with, partition, deep_map

class TestArrayChallengeAdvanced(unittest.TestCase):
    
    def test_compose(self):
        add1 = lambda x: x + 1
        mul2 = lambda x: x * 2
        
        # Test basic composition
        self.assertEqual(compose(add1, mul2)(5), 11)  # ((5 * 2) + 1)
        self.assertEqual(compose(mul2, add1)(5), 12)  # ((5 + 1) * 2)
        
        # Test with more functions
        add3 = lambda x: x + 3
        self.assertEqual(compose(add1, mul2, add3)(5), 13)  # (((5 + 3) * 2) + 1)
        
        # Test with no functions
        self.assertEqual(compose()(5), 5)  # Identity function
    
    def test_pipe(self):
        add1 = lambda x: x + 1
        mul2 = lambda x: x * 2
        
        # Test basic pipe
        self.assertEqual(pipe(add1, mul2)(5), 12)  # ((5 + 1) * 2)
        self.assertEqual(pipe(mul2, add1)(5), 11)  # ((5 * 2) + 1)
        
        # Test with more functions
        add3 = lambda x: x + 3
        self.assertEqual(pipe(add3, mul2, add1)(5), 17)  # (((5 + 3) * 2) + 1)
        
        # Test with no functions
        self.assertEqual(pipe()(5), 5)  # Identity function
    
    def test_memoize(self):
        # Test with simple function
        call_count = 0
        
        @memoize
        def expensive_func(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        self.assertEqual(expensive_func(5), 10)
        self.assertEqual(expensive_func(5), 10)
        self.assertEqual(call_count, 1)  # Function should only be called once for the same input
        
        self.assertEqual(expensive_func(6), 12)
        self.assertEqual(call_count, 2)  # Function should be called for a new input
        
        # Test with multiple arguments
        call_count_multi = 0
        
        @memoize
        def multi_arg_func(x, y):
            nonlocal call_count_multi
            call_count_multi += 1
            return x + y
        
        self.assertEqual(multi_arg_func(1, 2), 3)
        self.assertEqual(multi_arg_func(1, 2), 3)
        self.assertEqual(call_count_multi, 1)
        
        self.assertEqual(multi_arg_func(2, 1), 3)
        self.assertEqual(call_count_multi, 2)  # Different argument order should be a different call
    
    def test_zip_with(self):
        # Test with two arrays
        self.assertEqual(zip_with(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]), [5, 7, 9])
        
        # Test with three arrays
        self.assertEqual(zip_with(lambda x, y, z: x + y + z, [1, 2], [3, 4], [5, 6]), [9, 12])
        
        # Test with arrays of different lengths
        self.assertEqual(zip_with(lambda x, y: x + y, [1, 2, 3], [4, 5]), [5, 7])
        
        # Test with empty arrays
        self.assertEqual(zip_with(lambda x, y: x + y, [], []), [])
        self.assertEqual(zip_with(lambda x, y: x + y, [1, 2], []), [])
    
    def test_partition(self):
        # Test with numbers
        self.assertEqual(partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0), ([2, 4], [1, 3, 5]))
        
        # Test with strings
        self.assertEqual(
            partition(["apple", "banana", "cherry", "date"], lambda x: len(x) > 5),
            (["banana", "cherry"], ["apple", "date"])
        )
        
        # Test with all elements passing
        self.assertEqual(partition([2, 4, 6], lambda x: x % 2 == 0), ([2, 4, 6], []))
        
        # Test with no elements passing
        self.assertEqual(partition([1, 3, 5], lambda x: x % 2 == 0), ([], [1, 3, 5]))
        
        # Test with empty array
        self.assertEqual(partition([], lambda x: x > 0), ([], []))
    
    def test_deep_map(self):
        # Test with nested array
        self.assertEqual(deep_map([1, [2, [3, 4]], 5], lambda x: x * 2), [2, [4, [6, 8]], 10])
        
        # Test with flat array
        self.assertEqual(deep_map([1, 2, 3], lambda x: x * 2), [2, 4, 6])
        
        # Test with empty array
        self.assertEqual(deep_map([], lambda x: x * 2), [])
        
        # Test with deeply nested empty arrays
        self.assertEqual(deep_map([[], [[]]], lambda x: x * 2), [[], [[]]])


if __name__ == "__main__":
    print("Running tests for the Advanced Array Manipulation Challenge...")
    unittest.main() 