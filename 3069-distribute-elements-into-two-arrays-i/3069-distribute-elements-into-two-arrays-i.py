class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        l = 0
        r = 0
        for i in range(2,len(nums)):
            if arr1[l] > arr2[r]:
                arr1.append(nums[i])
                l += 1
            else:
                arr2.append(nums[i])
                r += 1
        return arr1 + arr2


        