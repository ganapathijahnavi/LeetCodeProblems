class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def subsetdiff(arr,diff):
            n = len(arr)
            dp = [[0 for _ in range(diff+1)]for _ in range(n+1)]
            for i in range(n+1):
                dp[i][0] = 1
            for i in range(1,n+1):
                for j in range(1,diff+1):
                    curr_num = arr[i-1]
                    not_take = dp[i-1][j]
                    if curr_num <= j:
                        take = dp[i-1][j-curr_num]
                    else:
                        take = 0
                    dp[i][j] = take + not_take
            return dp[n][diff] 
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        s1 = (total_sum + target )//2 
        zero_count = nums.count(0)
        non_zero_nums = [x for x in nums if x != 0]
        if s1 < 0:
            return 0
        return subsetdiff(non_zero_nums, s1) * (2 ** zero_count)
        