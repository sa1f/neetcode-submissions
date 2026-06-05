class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        map (target - num) => 
        4,0 
        3,1 
        2,2
        1,3

        go through array, check if target - curr exists in the map
        if it exists return [curr_index, map_index]
       
        """

        seen = {}

        for a_idx, a in enumerate(nums):
            b = target - a
            if b in seen:
                return [seen[b], a_idx]
            seen[a] = a_idx