class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def per(indx):
            if indx == len(nums) - 1:
                res.append(nums[:])
                return
            seen = set()
            for i in range(indx,len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[indx], nums[i] = nums[i], nums[indx]
                per(indx+1)
                nums[indx], nums[i] = nums[i], nums[indx]
            return 
        per(0)
        return res
        


        