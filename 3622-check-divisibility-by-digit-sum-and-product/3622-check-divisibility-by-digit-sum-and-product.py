class Solution:
    def checkDivisibility(self, n: int) -> bool:
        tot = 0
        prod = 1
        temp = n
        while temp > 0:
            rem = temp % 10
            tot += rem
            prod *= rem
            temp = temp // 10
        check = tot + prod
        if n % check == 0 :
            return True
        else:
            return False
        