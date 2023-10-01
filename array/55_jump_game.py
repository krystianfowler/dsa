# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        currPower = 0
        for idx, n in enumerate(nums):
            currPower -= 1
            if n == 0 and currPower < 1 and idx != len(nums) - 1:
                return False
            currPower = max(currPower, n)
        return True
