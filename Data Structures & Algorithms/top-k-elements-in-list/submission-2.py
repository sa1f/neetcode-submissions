"""
So the naive way to solve this is to keep track
 of the count of each number and then create a list
  from this map, sort by the count, and then take 
  the top three and return those values. 

nlogn
n - space


with a min heap

"""
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = [(-count, num) for num, count in count.items()]
        heapq.heapify(heap)

        res =[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        
    def topKFrequentSort(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        sorted_counts = sorted(count.items(), key=lambda kv: kv[1], reverse=True)

        return [kv[0] for kv in sorted_counts[:k]]

        



        
        