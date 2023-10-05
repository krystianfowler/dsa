# Space complexity: O(n)
# Time complexity: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        # First sweep left to right comparing ensuring each element satisfies condition with previous element
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candy[i] <= candy[i - 1]:
                candy[i] = candy[i - 1] + 1
        
        # Sweep again but reverse, ensuring each element satisfies condition with next
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i + 1] + 1
        candySum = sum(candy)
        return candySum
