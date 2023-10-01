# Space complexity: O(1)
# Time complexity: O(n), n - length of prices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            maxProfit = max(maxProfit, max(0, prices[right] - prices[left]))
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxProfit
