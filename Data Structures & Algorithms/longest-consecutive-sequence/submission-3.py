"""
Requirements:

nums - array of ints
return length of longest consecutive sequence of integers that can be formed

max_len
curr_max_len

curr = 2

guard: 
if len(nums) < 2: return len(nums)

sort array

set max_len = 0
set curr_len = 1
iterate through nums up until the second last nuum
  if next num is consecutive
    curr_len += 1
  else:
    update max_len
    set curr_len back to 1

complexity: nlogn, space complexity - o(1)

example: nums=[2,20,4,10,3,4,5]


  
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()

        max_len = 0
        curr_len = 1
        
        for idx,num in enumerate(nums[:-1]):
            print(f'idx: {idx}, num: {num}, max_len: {max_len}, curr_len: {curr_len}')
            if num == nums[idx + 1]:
                continue
            if num + 1 == nums[idx + 1]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
        return max(max_len,curr_len)






