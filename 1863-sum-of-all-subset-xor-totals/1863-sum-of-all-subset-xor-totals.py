class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        tot = 0
        def subsets(inp,out):
            nonlocal tot
            if len(inp) == 0:
                res = 0
                for num in out:
                    res ^= num
                tot += res
                return
            subsets(inp[1:], out)
            subsets(inp[1:], [inp[0]] + out)
            return tot
        return subsets(nums,[])

        