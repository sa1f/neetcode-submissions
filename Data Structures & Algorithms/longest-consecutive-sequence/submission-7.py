"""
Longest consecutive sequence

- nums - array of ints

return the length of the longest consecutive sequence of elements that can be formed.


requirements

max # of ints? min # of ints
min/max value of ints

ideas

- sort the list - O(nlogn) time 
- convert to a set to get unique items, then convert to a list
- keep a max consecutive length initialized at 1
- keep a current sequence length initialized at 1
- if len(nums) < 2, return len(nums)
- go through list, 2nd number onwards
	- if prev number was (curr_num - 1)
		increment current sequence length
	- elif prev number is the same:
		continue
	- else
		then update max consecutive length, reset current sequence length to zero

space complexity - O(n) if it's a new list


{
	2: (2)
	20: (20)
	4: (4)
}

[1,1,2,3]
curr_len = 3
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        sorted_nums = sorted(set(nums))

        max_len = 1
        curr_len = 1

        for i in range(1, len(sorted_nums)):
            prev_num = sorted_nums[i - 1]
            curr_num = sorted_nums[i]

            if prev_num == curr_num - 1:
                curr_len += 1
            else:
                curr_len = 1
            
            max_len = max(curr_len, max_len)

        return max_len