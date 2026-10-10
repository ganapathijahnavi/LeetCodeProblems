class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2
        if sum(diffs) <= total_k:
            return 0
        low , high = 0, max(diffs)
        best_max_diff = high
        while low <= high:
            mid = (low + high) // 2
            ops_needed = sum(d-mid for d in diffs if d > mid)
            if ops_needed <= total_k:
                best_max_diff = mid 
                high = mid - 1
            else:
                low = mid + 1
        rem_k = total_k
        final_diffs = []
        for d in diffs:
            if d > best_max_diff:
                reduction = d - best_max_diff
                if rem_k >= reduction:
                    rem_k -= reduction
                    final_diffs.append(best_max_diff)
                else:
                    final_diffs.append(d-rem_k)
                    rem_k = 0
            else:
                final_diffs.append(d)
        if rem_k > 0:
            new_final = []
            for d in final_diffs:
                if d == best_max_diff and rem_k > 0:
                    new_final.append(d-1)
                    rem_k -= 1
                else:
                    new_final.append(d)
            final_diffs = new_final
        return sum(d * d for d in final_diffs)