class Solution:
    def coinChange(self, arr: list[int], s: int) -> int:
        int_max = float("inf") 
        n = len(arr)
        dp = [[0 for _ in range(s+1)]for _ in range(n+1)]
        # for i in range(n + 1):
        #     dp[i][0] = 0
        for j in range(1,s+1):
            dp[0][j] = int_max
        for i in range(1,n+1):
            for j in range(1,s+1):
                curr_num = arr[i-1]
                not_take = dp[i-1][j]
                if curr_num <= j:
                    take = 1 + dp[i][j-curr_num]
                    dp[i][j] = min(take, not_take)
                else:
                    dp[i][j] = not_take

        if dp[n][s] == int_max:
            return -1
        return dp[n][s]