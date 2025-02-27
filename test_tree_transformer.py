import unittest
from tree_node import TreeNode
from tree_transformer import min_operations

class TestTreeTransformer(unittest.TestCase):
    
    def test_identical_trees(self):
        """Test case where both trees are identical."""
        tree1 = TreeNode.build_tree([1, 2, 3, 4, 5])
        tree2 = TreeNode.build_tree([1, 2, 3, 4, 5])
        self.assertEqual(min_operations(tree1, tree2), 0)
    
    def test_change_node_value(self):
        """Test case where only node values need to be changed."""
        tree1 = TreeNode.build_tree([1, 2, 3, 4, 5])
        tree2 = TreeNode.build_tree([1, 2, 6, 4, 7])
        self.assertEqual(min_operations(tree1, tree2), 2)  # Change 3 to 6 and 5 to 7
    
    def test_insert_nodes(self):
        """Test case where nodes need to be inserted."""
        tree1 = TreeNode.build_tree([1, 2, 3])
        tree2 = TreeNode.build_tree([1, 2, 3, 4, 5])
        self.assertEqual(min_operations(tree1, tree2), 2)  # Insert 4 and 5
    
    def test_delete_nodes(self):
        """Test case where nodes need to be deleted."""
        tree1 = TreeNode.build_tree([1, 2, 3, 4, 5])
        tree2 = TreeNode.build_tree([1, 2, 3])
        self.assertEqual(min_operations(tree1, tree2), 2)  # Delete 4 and 5
    
    def test_mixed_operations(self):
        """Test case where a mix of operations is needed."""
        tree1 = TreeNode.build_tree([1, 2, 3, 4, None, 6])
        tree2 = TreeNode.build_tree([1, 2, 5, 4, 7, None, 8])
        # Change 3 to 5, Insert 7, Delete 6, Insert 8
        self.assertEqual(min_operations(tree1, tree2), 4)
    
    def test_completely_different_trees(self):
        """Test case where trees are completely different."""
        tree1 = TreeNode.build_tree([1, 2, 3])
        tree2 = TreeNode.build_tree([4, 5, 6])
        # Either replace all nodes (3 changes) or delete all nodes from tree1 (3) and insert all nodes from tree2 (3)
        self.assertEqual(min_operations(tree1, tree2), 3)
    
    def test_empty_trees(self):
        """Test case with empty trees."""
        self.assertEqual(min_operations(None, None), 0)
        
        tree = TreeNode.build_tree([1, 2, 3])
        self.assertEqual(min_operations(None, tree), 3)  # Insert 3 nodes
        self.assertEqual(min_operations(tree, None), 3)  # Delete 3 nodes
    
    def test_complex_transformation(self):
        """Test a more complex transformation scenario."""
        tree1 = TreeNode.build_tree([10, 5, 15, 3, 7, 12, 20])
        tree2 = TreeNode.build_tree([10, 5, 18, 3, 8, 12, None, 1, 4])
        # Change 15 to 18, Change 7 to 8, Delete 20, Insert 1 and 4
        self.assertEqual(min_operations(tree1, tree2), 5)
    
    def test_unbalanced_trees(self):
        """Test with unbalanced trees."""
        # Create a deep left-skewed tree
        tree1 = TreeNode(1)
        current = tree1
        for i in range(2, 6):
            current.left = TreeNode(i)
            current = current.left
        
        # Create a deep right-skewed tree
        tree2 = TreeNode(1)
        current = tree2
        for i in range(2, 6):
            current.right = TreeNode(i)
            current = current.right
        
        # Need to delete 4 nodes from left tree and insert 4 nodes to right positions
        self.assertEqual(min_operations(tree1, tree2), 8)


if __name__ == "__main__":
    unittest.main() 