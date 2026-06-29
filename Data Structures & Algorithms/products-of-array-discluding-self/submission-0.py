"""
Requirements:
- int array of nums
- return an output of an array of nums where num at i, is the product 
  of all nums in array except nums[i]


Idea:

Create an output array [1,1,1...] (where number of 1s = num of elements in nums)

for num at idx in nums:
  in output array multiply existing number with the current number, unless we're
  at current idx

return output


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for idx, num in enumerate(nums):
            for output_idx in range(len(output)):
                if idx == output_idx:
                    continue
                output[output_idx] = output[output_idx] * num
        return output



        