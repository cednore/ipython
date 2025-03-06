"""
Advanced Array Manipulation Challenge

This challenge extends the basic array manipulation challenge with more complex operations.
It's designed for candidates who finish the basic challenge quickly or for assessing more senior candidates.

Instructions:
1. Implement all the required functions below
2. Each function has a description and examples
3. Run the tests using the separate test file: python test_array_challenge_advanced.py

Time: Additional 10-15 minutes
"""


def compose(*funcs):
    """
    Create a function that is the composition of a list of functions.
    Each function consumes the return value of the function that follows.

    Args:
        *funcs: Variable number of functions

    Returns:
        Function that is the composition of the input functions

    Example:
        add1 = lambda x: x + 1
        mul2 = lambda x: x * 2
        compose(add1, mul2)(5) -> 11  # ((5 * 2) + 1)
    """
    # Your code here
    pass


def pipe(*funcs):
    """
    Create a function that is the pipe of a list of functions.
    Each function consumes the return value of the function that precedes it.

    Args:
        *funcs: Variable number of functions

    Returns:
        Function that is the pipe of the input functions

    Example:
        add1 = lambda x: x + 1
        mul2 = lambda x: x * 2
        pipe(add1, mul2)(5) -> 12  # ((5 + 1) * 2)
    """
    # Your code here
    pass


def memoize(func):
    """
    Create a memoized version of a function.
    The function should cache its results for the same inputs.

    Args:
        func: Function to memoize

    Returns:
        Memoized function

    Example:
        @memoize
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        fibonacci(10) -> 55  # Much faster than without memoization
    """
    # Your code here
    pass


def zip_with(func, *arrays):
    """
    Apply a function to corresponding elements of multiple arrays.

    Args:
        func: Function to apply
        *arrays: Variable number of arrays

    Returns:
        New array with the function applied to corresponding elements

    Example:
        zip_with(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
    """
    # Your code here
    pass


def partition(arr, predicate):
    """
    Split an array into two arrays based on a predicate function.

    Args:
        arr: Array to partition
        predicate: Function that returns True/False for each element

    Returns:
        Tuple of two arrays: (elements that pass, elements that fail)

    Example:
        partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0) -> ([2, 4], [1, 3, 5])
    """
    # Your code here
    pass


def deep_map(arr, func, apply_to_non_lists=False):
    """
    Apply a function to each element in a deeply nested array.

    Args:
        arr: Nested array
        func: Function to apply
        apply_to_non_lists: Whether to apply the function to non-list elements

    Returns:
        New nested array with the function applied

    Example:
        deep_map([1, [2, [3, 4]], 5], lambda x: x * 2) -> [2, [4, [6, 8]], 10]
    """
    # Your code here
    pass
