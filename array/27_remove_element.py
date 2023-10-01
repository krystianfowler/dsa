# Space complexity: O(1)
# Time complexity: O(n), n - length of nums
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notValIdx = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[notValIdx] = nums[i]
                notValIdx += 1
        return notValIdx
