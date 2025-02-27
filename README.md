# Binary Tree Transformation Challenge

## Problem Statement

You are given a binary tree and a target binary tree. Your task is to find the minimum number of operations needed to transform the original tree into the target tree.

The allowed operations are:
1. **Delete a node**: Remove a leaf node from the tree.
2. **Insert a node**: Add a new leaf node to the tree.
3. **Change node value**: Modify the value of an existing node.

## Objective

Complete the implementation of the `min_operations` function in `tree_transformer.py` that calculates the minimum number of operations required to transform the original tree into the target tree.

## Constraints

- Each node in the tree has a value between 1 and 1000.
- The number of nodes in each tree is between 1 and 100.
- The solution should have optimal time and space complexity.

## Example

```
Original Tree:
    1
   / \
  2   3
 /
4

Target Tree:
    1
   / \
  2   5
 / \
4   6
```

The minimum operations required would be 2:
- Insert node with value 6 as right child of node 2
- Change node value from 3 to 5

## Testing

Run the tests to verify your solution:

```bash
python test_tree_transformer.py
```

## Evaluation Criteria

Your solution will be evaluated based on:
1. Correctness
2. Time and space complexity
3. Code quality and readability
4. Edge case handling

Good luck! 