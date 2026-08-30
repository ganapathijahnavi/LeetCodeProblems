class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i1 = nums.index(min(nums))
        i2 = nums.index(max(nums))
        low, high = min(i1,i2), max(i1,i2)
        return min(high + 1, n - low, (low+1) + (n-high))
        