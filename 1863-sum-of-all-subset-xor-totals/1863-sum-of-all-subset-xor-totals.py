class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(indx, res):
            if indx == len(nums):
                return res
            include = dfs(indx+1, res ^ nums[indx])
            exclude = dfs(indx+1, res)
            return include + exclude
        return dfs(0,0)

        