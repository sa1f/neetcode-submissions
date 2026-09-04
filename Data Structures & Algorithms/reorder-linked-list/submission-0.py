# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        
        stack = []
        result = []

        curr = head
        while curr:
            print(curr.val)
            stack.append(curr)
            curr = curr.next
        
        curr = head
        list_length = len(stack)
        while True:
            if len(result) < list_length:
                result.append(curr) 
                curr = curr.next
            else:
                break

            if stack:
                result.append(stack.pop())
            else:
                break

        curr = head
        for node in result[1:]:
            curr.next = node
            curr = node
        curr.next = None
        