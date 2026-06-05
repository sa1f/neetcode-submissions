"""
slow pointer, keeps track of the last non duplicate index
fast pointer, keeps going finds the next non duplicate index

if fast - slow > 1
  nums[slow + 1] = nums[fast]

nums = [1,1,2,3,4]

slow = 0
fast = 0

while fast < len(nums) - 2:
    prev = nums[fast]
    fast += 1
    curr = nums[fast]

    if prev == 

[1,2,3,4,4]

slow = 0
fast = 1
while 1 < 5:
    fast = 2

while 2 < 5:
  slow = 1
  fast = 3

while 3 < 5:
  slow = 2
  fast = 4

while 4 < 5:
    slow = 3
    fast = 5

--




"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
                continue
            else:
                nums[slow + 1] = nums[fast]
                slow += 1
                fast +=1

        return slow + 1

