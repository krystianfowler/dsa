# Space complexity: O(1)
# Time complexity: O(n), n - length of nums
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        for i in range(1, len(nums)): 
            if nums[right - 1] != nums[i]:
                nums[right] = nums[i]
                right += 1
                left = right
            elif right - left < 1:
                nums[right] = nums[i]
                right += 1
        return right
