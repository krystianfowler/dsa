# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if we actually have a solution
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gasTank, startIdx = 0, 0
        
        # Find the one unique solution, if gasTank becomes negative we restart
        for i in range(len(gas)):
            gasTank += gas[i] - cost[i]
            
            if gasTank < 0:
                startIdx = i+1
                gasTank = 0
            
        return startIdx
