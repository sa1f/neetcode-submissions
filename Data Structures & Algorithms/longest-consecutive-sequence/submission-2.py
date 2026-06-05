class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums) # [2,20,4,10,3,5]
        heads = []       # [2, 20 10]
        max_count = 0
        for num in nums:
            if num - 1 not in seen:
                heads.append(num)
        for num in heads:
            curr = num       # 2, 3, 4, 5
            curr_max = 0     # 0, 1, 2, 3

            while curr in seen:
                curr += 1
                curr_max += 1
            max_count = max(curr_max, max_count)
        return max_count

