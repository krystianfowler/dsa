# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        sumProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                sumProfit += prices[right] - prices[left]
            left = right
            right += 1
        return sumProfit
