class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)]for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1,amount+1):
                curr_num = coins[i-1]
                not_take = dp[i-1][j]
                if curr_num <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-curr_num]
                    # take = dp[i][j-curr_num]
                else:
                    dp[i][j] =  dp[i-1][j]
                    # take = 0
                # dp[i][j] = not_take + take
        return dp[n][amount]


        