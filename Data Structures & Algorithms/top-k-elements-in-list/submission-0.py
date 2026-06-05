"""
requirements:
nums, min/max value and len of arr
same with k, min/max value

first make a frequency map:

set a freq_map {}
go through list
    key is num, value is count

next use a min heap to keep track of the top k frequent items

heap = []

go through freq_map
    add to heap, using count as the key for the heap
    heap pop as heap gets > k

return heap values

freq_map {1:1, 2:2, 3:3}  o(n), o(n)
heap {2:2, 3:3} o(n * log(k)), o(n)

[2,3]


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 0
        heap = []
        for num, count in freq_map.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for count, num in heap:
            result.append(num)
        return result

        