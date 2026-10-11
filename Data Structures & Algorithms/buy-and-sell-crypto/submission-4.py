"""

I start parsing from left to right. With one pointer.
Look at the element next to the pointer. If it is greater max profit = next - pointer. Look at the element next to the next.
If it is smaller move the pointer as I can buy the stock for a lower price.

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
        