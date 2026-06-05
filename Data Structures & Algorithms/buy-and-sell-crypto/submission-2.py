"""
min: 0, 0
max: 0

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for num in prices:
            min_so_far = min(num, min_so_far)
            max_profit = max(max_profit, num - min_so_far)
        return max_profit