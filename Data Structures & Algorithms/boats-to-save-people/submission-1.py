"""
people = [5,1,4,2], limit = 6
[1,2,4,5]

step - 0
l = 0
r = 3
num_boats = 0

step - 1
l = 1
r = 2
num_boats = 1

step - 2
l = 2
r = 1
num_boats = 2

[1,3,2,3,2], limit = 3
[1,2,2,3,3]

step - 0
l = 0
r = 4
num_boats = 0

step - 1
l = 0
r = 3
num_boats = 1

step - 2
l = 0
r = 2
num_boats = 2

step - 2
l = 1
r = 1
num_boats = 3

num_boats = 4
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        num_boats = 0
        people.sort()

        while l < r:
            num_boats += 1
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            print(l,r, num_boats)
        if l == r:
            num_boats += 1
        
        return num_boats

            
        