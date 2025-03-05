import unittest
from path_finder import longest_increasing_path

class TestPathFinder(unittest.TestCase):
    
    def test_example_case(self):
        """Test the example case from the problem statement."""
        matrix = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]
        self.assertEqual(longest_increasing_path(matrix), 4)
    
    def test_single_cell(self):
        """Test with a single cell matrix."""
        matrix = [[1]]
        self.assertEqual(longest_increasing_path(matrix), 1)
    
    def test_row_matrix(self):
        """Test with a single row matrix."""
        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(longest_increasing_path(matrix), 5)
    
    def test_column_matrix(self):
        """Test with a single column matrix."""
        matrix = [[5], [4], [3], [2], [1]]
        self.assertEqual(longest_increasing_path(matrix), 1)
    
    def test_decreasing_matrix(self):
        """Test with a matrix where all paths are decreasing."""
        matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        self.assertEqual(longest_increasing_path(matrix), 1)
    
    def test_zigzag_path(self):
        """Test with a matrix that has a zigzag increasing path."""
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        self.assertEqual(longest_increasing_path(matrix), 9)
    
    def test_equal_values(self):
        """Test with a matrix that has equal adjacent values."""
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(longest_increasing_path(matrix), 1)
    
    def test_negative_values(self):
        """Test with a matrix that has negative values."""
        matrix = [
            [-9, -8, -7],
            [-6, -5, -4],
            [-3, -2, -1]
        ]
        self.assertEqual(longest_increasing_path(matrix), 9)
    
    def test_mixed_values(self):
        """Test with a matrix that has mixed positive and negative values."""
        matrix = [
            [-1, 0, 1],
            [-2, -1, 2],
            [-3, -2, 3]
        ]
        self.assertEqual(longest_increasing_path(matrix), 7)


if __name__ == "__main__":
    unittest.main() 