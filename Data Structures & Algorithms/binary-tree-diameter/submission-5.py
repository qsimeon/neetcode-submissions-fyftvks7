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
        if root.left is None:
            return 0
        else:
            maxLeft = max(self.leftHeight(root.left), self.rightHeight(root.left))
            return 1 + maxLeft
    
    def rightHeight(self, root: Optional[TreeNode]) -> int:
        """
        Height of right branch. Equal to number of edges from root to leaf,
        or number of nodes less not including root.
        """
        if root.right is None:
            return 0
        else:
            maxRight = max(self.leftHeight(root.right), self.rightHeight(root.right))
            return 1 + maxRight

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = -float("inf")
        # calls iter(root) implicitly
        for node in root: 
            if node: 
                # node has a val
                leftHeight = self.leftHeight(node)
                rightHeight = self.rightHeight(node)
                print(f"node: {node.val},\t leftHeight: {leftHeight},\t rightHeight:{rightHeight}\n")
                height = leftHeight + rightHeight
                if height > maxHeight:
                    maxHeight = height
            else: 
                # node is None
                continue
        return maxHeight

        