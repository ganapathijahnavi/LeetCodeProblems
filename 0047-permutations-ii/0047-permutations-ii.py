class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def subset(indx):
            if indx == len(nums) - 1:
                # if nums not in res:
                res.append(nums[:])
                return
            check = set()
            for i in range(indx,len(nums)):
                if nums[i] in check:
                    continue
                check.add(nums[i])
                nums[indx], nums[i] = nums[i], nums[indx]
                subset(indx + 1)
                nums[indx], nums[i] = nums[i], nums[indx]
            return 
        subset(0)
        return res
        