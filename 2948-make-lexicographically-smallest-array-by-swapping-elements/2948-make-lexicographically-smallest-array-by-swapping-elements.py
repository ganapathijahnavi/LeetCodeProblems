from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sorted_pairs[j + 1][0] - sorted_pairs[j][0] <= limit:
                j += 1
         
            component_vals = [sorted_pairs[k][0] for k in range(i, j + 1)]
            component_indices = sorted(sorted_pairs[k][1] for k in range(i, j + 1))
            
            for val, idx in zip(component_vals, component_indices):
                result[idx] = val
                
            i = j + 1
            
        return result