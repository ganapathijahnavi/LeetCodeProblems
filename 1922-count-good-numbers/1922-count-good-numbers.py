MOD = 10 ** 9 + 7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 4 == 0:
            half = self.countGoodNumbers(n//2)
            return half * half % MOD
        if n % 2 == 0:
            return self.countGoodNumbers(n-1) * 4 % MOD
        return 5 if n == 1 else self.countGoodNumbers(n-1) * 5 % MOD
        