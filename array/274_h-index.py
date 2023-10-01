# Space complexity: O(1)
# Time complexity: O(nlogn)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() # O(nlogn)
        hIdx = 0
        for idx, n in enumerate(citations): # O(n)
            if len(citations) - idx <= n:
                hIdx = max(hIdx,len(citations) - idx)
        return hIdx
