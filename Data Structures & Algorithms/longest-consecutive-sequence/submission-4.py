"""
Longest consecutive sequence

- nums - array of ints

return the length of the longest consecutive sequence of elements that can be formed.


requirements

max # of ints? min # of ints
min/max value of ints

ideas

- sort the list - O(nlogn) time 
- keep a max consecutive length initialized at zero
- keep a current sequence length initialized at 0
- go through list
	- if next number is consecutive
		increment current sequence length
	- elif next number is the same:
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

        nums.sort()

        max_len = 0
        curr_len = 0

        print(nums)
        for i in range(len(nums)):
            curr_len += 1
            if i == len(nums) - 1:
                continue
            curr_num = nums[i]
            next_num = nums[i + 1]

            print(f'{curr_num} {next_num} {curr_len}')


            if curr_num == next_num:
                curr_len -= 1
            elif curr_num + 1 == next_num:
                continue
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        return max(max_len, curr_len)
