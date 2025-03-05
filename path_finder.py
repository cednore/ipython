from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    """
    Find the length of the longest increasing path in the matrix.
    
    An increasing path is a path where each cell's value is greater than the previous cell's value.
    You can move up, down, left, or right from any cell.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers.
        
    Returns:
        int: The length of the longest increasing path.
    """
    # TODO: Implement this function
    # This problem can be solved using DFS with memoization
    
    # Hint 1: For each cell, explore all four directions
    # Hint 2: Use memoization to avoid recalculating paths
    # Hint 3: The longest path can start from any cell
    
    # Your implementation here
    pass


# Helper functions you might want to implement:

def is_valid_cell(matrix: List[List[int]], row: int, col: int) -> bool:
    """
    Check if a cell is within the bounds of the matrix.
    
    Args:
        matrix (List[List[int]]): The matrix to check against.
        row (int): The row index.
        col (int): The column index.
        
    Returns:
        bool: True if the cell is valid, False otherwise.
    """
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


# The four possible directions: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 