from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # subarray_counts = defaultdict(int)
        # for i in range(len(nums)-k+1):
        #     window = nums[i : i + k]
        #     for num in set(window):
        #         subarray_counts[num] += 1
        # miss_ele = -1
        # for num, val in subarray_counts.items():
        #     if val == 1:
        #         miss_ele = max(miss_ele,num)
        # return miss_ele
        n = len(nums)
        counts = Counter(nums)
        if k == 1:
            ans = -1
            for num,cnt in counts.items():
                if cnt == 1:
                    ans = max(ans,num)
            return ans
        if k == n:
            return max(nums)
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans,nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans,nums[-1])
        return ans



        