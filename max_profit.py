"""
LeetCode Problem: 121. Best Time to Buy and Sell Stock  
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
- Iterate through the prices while keeping track of the minimum price seen so far.
- At each step, compute the profit if we sold today (current price - min price so far).
- Update the maximum profit accordingly.
- This ensures a one-pass O(n) solution with O(1) extra space.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Found a new lower price to buy
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)  # Update max profit

        return max_profit
