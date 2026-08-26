# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
head = None
curr_first = list1
curr_second = list2

if not curr_first:
    return curr_second
if not curr_second:
    return curr_first

if curr_first.val <= curr_second.val:
    head = curr_first
    curr_first = curr_first.next
else:
    head = curr_second
    curr_second = curr_second.next

curr = head

while curr_first and curr_second:
    if curr_first.val <= curr_second.val:
        curr.next = curr_first
        curr_first = curr_first.next
    else:
        curr.next = curr_second
        curr_second = curr_second.next
    
    curr = curr.next

return head

===

head = 1 > 1 > 2 > 3 > 4
curr_first = None
curr_second = 5
curr = 3

    
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr_first = list1
        curr_second = list2

        while curr_first and curr_second:
            if curr_first.val <= curr_second.val:
                curr.next = curr_first
                curr_first = curr_first.next
            else:
                curr.next = curr_second
                curr_second = curr_second.next
            
            curr = curr.next

        if curr_first:
            curr.next = curr_first
        elif curr_second:
            curr.next = curr_second
        
        return dummy.next