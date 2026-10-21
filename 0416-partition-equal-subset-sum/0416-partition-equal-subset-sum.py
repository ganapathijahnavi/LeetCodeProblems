class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def subsetsum(arr,tar):
            n = len(arr)
            dp = [[False for _ in range(tar+1)]for _ in range(n+1)]
            for i in range(n+1):
                dp[i][0] = True
            for i in range(1,n+1):
                for j in range(1,tar+1):
                    curr_num = arr[i-1]
                    not_take = dp[i-1][j]
                    if curr_num <= j:
                        take = dp[i-1][j-curr_num]
                    else:
                        take = False
                    dp[i][j] = take or not_take
            return dp[n][tar]
        if sum(nums) % 2 != 0:
            return False
        else:
            return subsetsum(nums, sum(nums)// 2)
        