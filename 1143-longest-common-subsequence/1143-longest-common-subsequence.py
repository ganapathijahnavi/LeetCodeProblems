class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(x,y,n,m,dp):
            if n == 0 or m == 0:
                return 0
            if dp[n][m] != -1:
                return dp[n][m]
            if x[n-1] == y[m-1]:
                dp[n][m] = 1 + lcs(x,y,n-1,m-1,dp)
            else:
                dp[n][m] = max(lcs(x,y,n-1,m,dp), lcs(x,y,n,m-1,dp))
            return dp[n][m]
        n = len(text1)
        m = len(text2)   
        dp = [[-1 for _ in range(m+1)]for _ in range(n+1)]
        return lcs(text1, text2, n, m,dp)
        