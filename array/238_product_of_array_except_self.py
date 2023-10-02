# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        out[0] = 1
        # First swipe, populate with prefix product for each number
        for i in range(1, len(nums)):
            out[i] = nums[i - 1] * out[i - 1]
        # Second swipe, calculate postfix and and fill final value
        currPostFix = 1 
        for i in range(len(nums) - 1, -1, -1):
           out[i] = currPostFix * out[i]
           currPostFix *= nums[i]
        return out
