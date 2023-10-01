# Space complexity: O(1)
# Time complexity: O(n), n - length of nums
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftPointer = 1
        for rightPointer in range(1, len(nums)):
            if nums[leftPointer - 1] != nums[rightPointer]:
                nums[leftPointer] = nums[rightPointer]
                leftPointer += 1
        return leftPointer
