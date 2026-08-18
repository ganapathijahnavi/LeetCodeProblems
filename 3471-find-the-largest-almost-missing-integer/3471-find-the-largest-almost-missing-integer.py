from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_counts = defaultdict(int)
        for i in range(len(nums)-k+1):
            window = nums[i : i + k]
            for num in set(window):
                subarray_counts[num] += 1
        miss_ele = -1
        for num, val in subarray_counts.items():
            if val == 1:
                miss_ele = max(miss_ele,num)
        # return cnt_freq
        return miss_ele


        