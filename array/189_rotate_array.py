# Space complexity: O(1)
# Time complexity: O(n), n - length of nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # rotate by three reversals
        self.reverse(nums, 0, n - 1) # reverse whole array, the k-sized subarrays are now in place

        self.reverse(nums, 0, k - 1) # reverse first k elements

        self.reverse (nums, k, n - 1) # reverse remining n - k elements

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
