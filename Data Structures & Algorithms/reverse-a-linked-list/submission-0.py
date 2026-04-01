# Definition for singly-linked list.
from copy import deepcopy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        # make stack all disconnected leaf nodes initially
        stack = [None]
        while True:
            stack.append(ListNode(head.val, None))
            if head.next is None:
                break
            elif isinstance(head.next, ListNode):
                head = head.next
        
        # print(stack) # DEBUG
        # reverse the stack and connect the nodes to each other
        rev_stack = stack[::-1] # last node is None
        for curr_node, next_node in zip(rev_stack[:-1], rev_stack[1:]):
            curr_node.next = next_node
        
        # first node of rev_stack is the new head node
        return rev_stack[0]