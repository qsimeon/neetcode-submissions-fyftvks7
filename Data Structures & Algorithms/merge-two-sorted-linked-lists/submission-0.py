# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        dummy = ListNode(val=None, next=None)

        ptr1 = list1
        ptr2 = list2
        tail = dummy
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            elif ptr1.val > ptr2.val:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next
        # one pointer ar end, append the rest
        if ptr1 is None and ptr2 is not None:
            tail.next = ptr2 
        if ptr2 is None and ptr1 is not None:
            tail.next = ptr1
        return dummy.next
























# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         # Base case: one or both of the lists are empty
#         if not list1:
#             return list2
#         elif not list2:
#             return list1
        
#         # Compare (list1[0]) <-> (list1[1], list2[0])
#         dummy = ListNode()
#         tail = dummy # will store our merged lst
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else: # list2.val < list1.val
#                 tail.next = list2
#                 list2 = list2.next

#             # update tail pointer
#             tail = tail.next
        
#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2

#         return dummy.next