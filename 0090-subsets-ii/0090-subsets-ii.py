class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def subsets(inp_nums, out_nums):
            if len(inp_nums) == 0:
                res.append(out_nums)
                return
            count = 1
            while count < len(inp_nums) and inp_nums[count] == inp_nums[0]:
                count += 1

            subsets(inp_nums[1:], out_nums+[inp_nums[0]])
            subsets(inp_nums[count:], out_nums)
        subsets(nums, [])
        return res
        