# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
q = [(root, max, min)]

while q:
    curr, max, min = q.pop(0)

    left = curr.left
    right = curr.right

    if left:
        if left.val > curr.val:
            return False
        if max is not None:
            if left.val > max:
                return False
    if right:
        if right.val < curr.val:
            return False
        if max is not None:
            if right.val > max:
                return False
    
    
    if min is not None:
        if right.val < min or right.val < min:
            return False

    

    


"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = [(root, math.inf, -math.inf)]

        while q:
            curr, max_val, min_val = q.pop(0)

            if not (min_val < curr.val < max_val):
                return False

            if curr.left:
                q.append((curr.left, curr.val, min_val))
            if curr.right:
                q.append((curr.right, max_val, curr.val))

        return True
        