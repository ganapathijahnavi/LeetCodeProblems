class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        lcm_subsets = []
        for r in range(1, n + 1):
            for comb in combinations(coins, r):
                lcm_val = comb[0]
                for c in comb[1:]:
                    lcm_val = (lcm_val * c) // math.gcd(lcm_val, c)
                sign = 1 if r % 2 == 1 else -1
                lcm_subsets.append((lcm_val, sign))
     
        def count_amounts(x: int) -> int:
            total = 0
            for lcm_val, sign in lcm_subsets:
                total += sign * (x // lcm_val)
            return total

       
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        