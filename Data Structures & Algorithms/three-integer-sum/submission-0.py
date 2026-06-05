"""
if you're at -1, you need two numbers that add up to +1 

[0,1,2,-1,-4], target is 1

{
    
    -4: 4
}

[0,1],  [2,3]


[-4, -1, -1, 0,1,2]
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]

            while l < r:
                curr_sum = nums[l] + nums[r]

                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums [r + 1]:
                        r -= 1

        return result
                


                
        