# Space complexity: O(1)
# Time complexity: O(m + n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1Idx = m - 1
        n2Idx = n - 1
        for i in range(m + n - 1 , -1, -1):
            if n1Idx >= 0 and (n2Idx < 0 or nums1[n1Idx] > nums2[n2Idx]):
                nums1[i] = nums1[n1Idx]
                n1Idx -= 1
            else: 
                nums1[i] = nums2[n2Idx]
                n2Idx -= 1
