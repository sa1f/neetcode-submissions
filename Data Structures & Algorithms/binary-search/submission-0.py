"""
left and right pointer

while l < r
    mid = mid // 2


[-1,0,2,4,6,8], target = 4

l   = 0, 2
r   = 5, 5
mid = 2, 3

nums = [-1,0,2,4,6,8], target = 3

l.  = 0, 2, 2
r.  = 5, 5, 3
mid = 2, 3, 3


"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1
        