class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # n = len(arr)
        # total = 0
        # for i, val in enumerate(arr):
        #     total_subarrays = (i + 1) * (n - i)
        #     odd_count = (total_subarrays + 1) // 2
        #     total += val * odd_count
        # return total
        res = 0
        n = len(arr)
        def solve(i,j):
            nonlocal res
            if j >= n:
                return
            if (j-i+1)%2 == 1:
                res += sum(arr[i:j+1])
            solve(i,j+1)
        for i in range(n):
            solve(i,i)
        return res        
