# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        """Depth first search iteration over tree."""
        yield self
        if self.left is not None:
            yield from self.left
        if self.right is not None:
            yield from self.right
        # if both None, go back
        yield None

class Solution:
    def leftHeight(self, root: Optional[TreeNode]) -> int:
        """
        Height of left branch. Equal to number of edges from root to leaf,
        or number of nodes less not including root.
        """
        if root is None or root.left is None:
            return 0
        else:
            maxLeft = max(self.leftHeight(root.left), self.rightHeight(root.left))
            return 1 + maxLeft
    
    def rightHeight(self, root: Optional[TreeNode]) -> int:
        """
        Height of right branch. Equal to number of edges from root to leaf,
        or number of nodes less not including root.
        """
        if root is None or root.right is None:
            return 0
        else:
            maxRight = max(self.leftHeight(root.right), self.rightHeight(root.right))
            return 1 + maxRight

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        For every node, calculate the absolute difference in 
        height of the left and right branch. If any evaluates
        to more than 1 return false immediately.
        """
        if root is None:
            return True
        for node in root:
            lh = self.leftHeight(node)
            rh = self.rightHeight(node)
            if abs(lh - rh) > 1:
                return False
        return True

    