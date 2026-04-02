# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if it is a root maxDepth is 1
        if not root.left and not root.right:
            return 1
        # one side only
        if root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        if root.right and not root.left:
            return 1 + self.maxDepth(root.right)
        # both sides present
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        