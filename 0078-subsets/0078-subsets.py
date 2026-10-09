class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # def backtrack(index: int, current_subset: List[int]):
        #     result.append(list(current_subset))
        #     for i in range(index, len(nums)):
        #         current_subset.append(nums[i])
        #         backtrack(i + 1, current_subset)
        #         current_subset.pop()
            
        # backtrack(0, [])
        # return result
        res = []
        def recur(inp, out):
            if len(inp) == 0:
                res.append(out)
                return
            recur(inp[1:], out)
            recur(inp[1:], out + [inp[0]])
        recur(nums,[])
        return res


        