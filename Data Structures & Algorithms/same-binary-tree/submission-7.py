# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isLeafNode(x: Optional[TreeNode]):
    if x.left is None and x.right is None:
        return True
    return False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases where at least one of the nodes is None
        if p is None and q is None:
            return True
        if isinstance(p, TreeNode) and q is None:
            return False
        if p is None and isinstance(q, TreeNode):
            return False
        
        # If both are leaf nodes, they are equivalent if they have the same value
        if isLeafNode(p) and isLeafNode(q):
            return p.val == q.val
        # If one is a leaf and the other is not, they are not equal
        if isLeafNode(p) and not isLeafNode(q): 
            return False
        if not isLeafNode(p) and isLeafNode(q): 
            return False
        # Otherwise the trees are equal if their left is equal and their right is equal
        if (p.left is not None) and (q.left is not None): 
            left_eq = self.isSameTree(p.left, q.left)
        elif (p.left is None) and (q.left is None):
            left_eq = True
        else:
            left_eq = False
        if (p.right is not None) and (q.right is not None): 
            right_eq = self.isSameTree(p.right, q.right)
        elif (p.right is None) and (q.right is None):
            right_eq = True
        else: 
            right_eq = False
        return (left_eq and right_eq)
        