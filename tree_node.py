class TreeNode:
    """
    Binary tree node class.
    
    Attributes:
        val (int): The value of the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """
    
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a new TreeNode.
        
        Args:
            val (int): The value of the node.
            left (TreeNode): The left child of the node.
            right (TreeNode): The right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        """
        Check if two trees are structurally identical with the same node values.
        
        Args:
            other (TreeNode): The other tree to compare with.
            
        Returns:
            bool: True if the trees are identical, False otherwise.
        """
        if not other or not isinstance(other, TreeNode):
            return False
        
        return (self.val == other.val and
                ((self.left is None and other.left is None) or 
                 (self.left and other.left and self.left == other.left)) and
                ((self.right is None and other.right is None) or 
                 (self.right and other.right and self.right == other.right)))
    
    @staticmethod
    def build_tree(values):
        """
        Build a binary tree from a list of values in level order.
        
        Args:
            values (list): List of values in level order. None represents no node.
            
        Returns:
            TreeNode: The root of the constructed binary tree.
        """
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root 