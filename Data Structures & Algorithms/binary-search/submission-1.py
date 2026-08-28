"""

left = 0
right = len(nums) - 1

while right >= left:
    mid = (right + left) // 2
    if target > nums[mid]:
        left = mid
    elif target < nums[mid]:
        right = mid
    else:
        return mid
return -1


left  = 0 > 
right = 5 
mid   = 2 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid -1
            else:
                return mid
        return -1
        