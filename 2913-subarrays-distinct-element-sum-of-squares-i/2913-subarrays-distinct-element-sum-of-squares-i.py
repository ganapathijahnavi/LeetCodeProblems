class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res =  []
        ans = 0
        def subsets(start, end, curr_arr):
            if end == len(nums):   
                return
            curr_arr.append(nums[end])
            res.append(curr_arr[:])
            subsets(start, end+1, curr_arr)
            curr_arr.pop()
            return 
        for i in range(len(nums)):
            subsets(i,i,[])
        for num in res:
            ans += len(set(num)) ** 2
        return ans
        
        