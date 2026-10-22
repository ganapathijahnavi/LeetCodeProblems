class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        n = len(nums)
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            rob_current = nums[i] + dp(i + 2)
            skip_current = dp(i + 1)
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        return dp(0) 


        

        