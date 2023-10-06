# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        # Formula for water trapped on single cell is min(maxLeft, maxRight) - height[i]
        # We could do a double sweep and compute maxLeft, maxRight for each position
        # But since we only care about the min of maxLeft and maxRight
        # We can use two pointers to do it in a single sweep and O(1) memory
        left, right = 0, len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        totalWater = 0
        while left < right:
            if maxLeft < maxRight:
                left += 1
                totalWater += max(0, maxLeft - height[left])
                maxLeft = max(maxLeft, height[left])
            else: 
                right -= 1
                totalWater += max(0, maxRight - height[right])
                maxRight = max(maxRight, height[right])
        return totalWater
