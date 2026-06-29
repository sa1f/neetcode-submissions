"""
Requirements:
- int array of nums
- return an output of an array of nums where num at i, is the product 
  of all nums in array except nums[i]


Idea:

products_at_left = [1]

i = 0, 1


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_at_left = [1]
        products_at_right = [1] * len(nums)

        for i in range(1, len(nums)):
            products_at_left.append(products_at_left[i - 1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            products_at_right[i] = products_at_right[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(products_at_left[i] * products_at_right[i])
        return result

        