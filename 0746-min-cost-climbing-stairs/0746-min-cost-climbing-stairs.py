class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        n = len(cost)
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))