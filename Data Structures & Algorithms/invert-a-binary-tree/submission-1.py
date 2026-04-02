# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root is a leaf node 

        if root is None or (not root.left and not root.right):
            return root
        # left is a tree, right is a leaf
        elif root.left and not root.right: 
            root.right = self.invertTree(root.left)
            root.left = None
        # left is a root, right is a tree
        elif not root.left and root.right:
            root.left = self.invertTree(root.right)
            root.right = None
        # both are trees
        else: 
            # pointers to prevent aliasing
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left = left
            root.right = right
        return root

        