# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        left = right = 0
        while left < len(nums) - 1:
            farthestLeap = left + nums[left]
            if farthestLeap >= len(nums) - 1:
                return count + 1
            # For current possibilities find one resulting in longest range
            maxRange = 0
            for idx in range(left + 1, min(len(nums) - 1, farthestLeap + 1)):
                currRange = idx + nums[idx]
                if currRange > maxRange: 
                    maxRange = currRange
                    right = idx
            # We can now leap to right pointer
            count += 1
            left = right
        return count
