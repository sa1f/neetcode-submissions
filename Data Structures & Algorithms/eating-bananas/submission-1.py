"""
piles -> piles[i] # of bananas in the ith pile
h     -> number of hours i have to eat all the bananas
k     -> banana per hour eating rate

at each hour i can choose a pile and eat up to k bananas


for # of bananas i pile if they are...
>= k
- eat up to k bananas in the pile
< k
- finish eating the pile, cannot move onto another pile

return the minimum integer k such that i can eat all bananas within h hours


piles = [1,4,3,2], h = 9

total # of bananas = 10 -> ceil(10/9) = 2 (minimum possible value for k assuming bananas are equally distributed)

lets sort

[1,2,3,4]

curr_k

t = 0, i = 0, pile fully eaten
t = 1, i = 1, pile fully eaten
t = 2, i = 2, 2 bananas eaten
t = 3, i = 2, 1 banana eaten (pile fully eaten)
t = 4, i = 3, 2 banana eaten 
t = 5, i = 3, 2 banana eaten  (pile fully eaten)

k = # of bananas / hour
h = # of hours


---

piles = [4,10,23,25], h = 4

ceil(62 / 4) = 16

4/


min k = 1
max k = # of bananas in the biggest pile

let's say we had a function to calc total_hours for a given k
we would just need to find the minimium feasible value of k 

we can binary search for this value between the min and max values of k
"""

from math import ceil
class Solution:
    def total_hours(self, k, piles):
        hours = 0

        for pile in piles:
            hours += ceil(pile / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = self.total_hours(mid, piles)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
        