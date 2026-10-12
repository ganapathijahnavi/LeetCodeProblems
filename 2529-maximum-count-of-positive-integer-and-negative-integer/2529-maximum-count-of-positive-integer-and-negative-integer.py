class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid 
        neg_count = left

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        pos_count = len(nums) - left 
        return max(neg_count, pos_count)
        