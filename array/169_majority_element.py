# Boyer-Moore voting algorithm
# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums: 
            if not candidate:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = None
        return candidate
