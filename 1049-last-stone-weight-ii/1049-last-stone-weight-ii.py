class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total_sum = sum(stones)
        tar = total_sum // 2
        n = len(stones)
        dp = [[False for _ in range(tar+1)]for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1,tar+1):
                curr_sum = stones[i-1]
                not_take = dp[i-1][j]
                if curr_sum <= j:
                    take = dp[i-1][j-curr_sum]
                else:
                    take = False
                dp[i][j] = not_take or take
     
        max_subset_sum = 0
        for j in range(tar,-1,-1):
            if dp[n][j]:
                max_subset_sum = j
                break
        return total_sum - 2*max_subset_sum

            
        