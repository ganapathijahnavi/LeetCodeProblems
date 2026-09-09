class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        hash_map = {}
        ans = 0
        if len(nums1) != len(nums2):
            return -1
        for i in nums1:
            hash_map[i] = hash_map.get(i,0) + 1
        for j in nums2:
            hash_map[j] = hash_map.get(j,0) - 1
        diff_sum = 0
        for key, diff in hash_map.items():
            if diff % 2 != 0:
                return -1
            diff_sum += abs(diff)
        return diff_sum // 4