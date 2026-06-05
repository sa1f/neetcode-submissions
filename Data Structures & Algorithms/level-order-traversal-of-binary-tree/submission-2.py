# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        if root:
            q.append((root, 0))
        level = -1
        results = []

        while q:
            curr_node, curr_level = q.pop(0)

            if level != curr_level:
                level = curr_level
                results.append([])

            results[-1].append(curr_node.val)

            if curr_node.left:
                q.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                q.append((curr_node.right, curr_level + 1))
        
        return results