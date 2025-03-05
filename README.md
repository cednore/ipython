# Matrix Path Finder Challenge

## Problem Statement

You are given a matrix of integers. Your task is to find the length of the longest increasing path in the matrix.

An increasing path is a path where each cell's value is greater than the previous cell's value. You can move up, down, left, or right from any cell.

## Objective

Complete the implementation of the `longest_increasing_path` function in `path_finder.py` that calculates the length of the longest increasing path in the given matrix.

## Constraints

- The matrix will have dimensions between 1x1 and 100x100.
- The values in the matrix will be integers between -10^9 and 10^9.
- You can only move in four directions: up, down, left, or right.

## Example

```
Input Matrix:
[
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]

Output: 4

Explanation: The longest increasing path is [1, 2, 6, 9].
Starting from matrix[2][1] -> matrix[2][0] -> matrix[1][0] -> matrix[0][0].
```

## Testing

Run the tests to verify your solution:

```bash
python test_path_finder.py
```

## Evaluation Criteria

Your solution will be evaluated based on:
1. Correctness
2. Time and space complexity
3. Code quality and readability
4. Edge case handling

Good luck! 