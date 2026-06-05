"""
numbers -> min length, max length, min/max values
target -> min/max values


l, r pointers

while l < r
    if nums[r] > target:
        r -= 1
        continue

    sum = nums[l] + nums[r]
    if sum == target:
        return [l + 1, r + 1]
    elif sum >  target:
        r -= 1
    elif sum < target:
        l += 1


    
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
        