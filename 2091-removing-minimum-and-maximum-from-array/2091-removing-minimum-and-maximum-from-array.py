class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_ele = float("inf")
        max_ele = float("-inf")
        min_indx, max_indx = 0, 0
        for i in range(len(nums)):
            if nums[i] < min_ele:
                min_indx = i
                min_ele = nums[i]
            if nums[i] > max_ele:
                max_indx = i
                max_ele = nums[i]
        if min_indx > max_indx:
            temp = min_indx
            min_indx = max_indx
            max_indx = temp

        from_left = max_indx + 1
        from_right = len(nums) - min_indx 
        from_both = (min_indx + 1) + (len(nums) - max_indx )

        return min(from_left,from_right,from_both)
        
        