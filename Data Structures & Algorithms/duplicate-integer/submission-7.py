"""
Requirements:

Ideas:

if len(nums) <= 1:
    return False

maintain a set, 
    go through each item, 
        check if num in set, 
            if so return true, 
            if not, add to set

Space - O(n)
time - O(n)




"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.save_space(nums)

    def default(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    def save_space(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        nums.sort()

        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx +1]:
                return True
        return False
