"""

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price=101
        maximum_price=0
        max_profit=-1
        for i in prices:
            if i<minimum_price:
                minimum_price=i
                maximum_price=i
            if i>maximum_price:
                maximum_price=i
            max_profit=max(max_profit,maximum_price-minimum_price)
        return max_profit
        