# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = []
        if root:
            s.append((root, 1))
        max_level = 0

        while s:
            curr_node, curr_level = s.pop()
            max_level = max(max_level, curr_level)

            if curr_node.left:
                s.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                s.append((curr_node.right, curr_level + 1))

        return max_level


