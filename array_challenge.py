"""
Array Manipulation Challenge

This challenge tests your ability to manipulate arrays (lists) in Python,
similar to JavaScript's map, reduce, and filter functions.

Instructions:
1. Implement all the required functions below
2. Each function has a description and examples
3. You can use built-in functions, but the goal is to demonstrate your understanding
   of how these operations work
4. Run the tests using the separate test file: python test_array_challenge.py

Time: 10-15 minutes
"""


def my_map(arr, func):
    """
    Implement a function similar to JavaScript's Array.map()

    Args:
        arr: List of elements
        func: Function to apply to each element

    Returns:
        New list with the function applied to each element

    Example:
        my_map([1, 2, 3], lambda x: x * 2) -> [2, 4, 6]
    """
    # Your code here
    pass


def my_filter(arr, func):
    """
    Implement a function similar to JavaScript's Array.filter()

    Args:
        arr: List of elements
        func: Function that returns True/False for each element

    Returns:
        New list with only the elements that pass the filter function

    Example:
        my_filter([1, 2, 3, 4], lambda x: x % 2 == 0) -> [2, 4]
    """
    # Your code here
    pass


def my_reduce(arr, func, initial=None):
    """
    Implement a function similar to JavaScript's Array.reduce()

    Args:
        arr: List of elements
        func: Function that takes accumulator and current value
        initial: Initial value for accumulator (optional)

    Returns:
        Single value after reduction

    Example:
        my_reduce([1, 2, 3], lambda acc, curr: acc + curr, 0) -> 6
    """
    # Your code here
    pass


def flatten_array(arr):
    """
    Flatten a nested array (list of lists) into a single list

    Args:
        arr: Nested list (can have multiple levels of nesting)

    Returns:
        Flattened list

    Example:
        flatten_array([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
    """
    # Your code here
    pass


def group_by(arr, key_func):
    """
    Group array elements by a key

    Args:
        arr: List of elements
        key_func: Function that returns the key to group by

    Returns:
        Dictionary with keys as group names and values as lists of elements

    Example:
        group_by([1, 2, 3, 4, 5], lambda x: 'even' if x % 2 == 0 else 'odd')
        -> {'even': [2, 4], 'odd': [1, 3, 5]}
    """
    # Your code here
    pass


def chain_operations(arr):
    """
    Chain multiple array operations:
    1. Filter out odd numbers
    2. Map remaining numbers to their squares
    3. Reduce to find the sum

    Args:
        arr: List of integers

    Returns:
        Sum of squares of even numbers

    Example:
        chain_operations([1, 2, 3, 4]) -> 20 (2² + 4² = 4 + 16 = 20)
    """
    # Your code here
    # You can use your functions above or Python built-ins
    pass
