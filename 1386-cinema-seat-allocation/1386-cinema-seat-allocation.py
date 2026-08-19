from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = defaultdict(int)
        
        for row, col in reservedSeats:
            if col in (2, 3):
                row_masks[row] |= 1  
            elif col in (4, 5):
                row_masks[row] |= 3  
            elif col in (6, 7):
                row_masks[row] |= 6  
            elif col in (8, 9):
                row_masks[row] |= 4  
     
        ans = (n - len(row_masks)) * 2
        
        for mask in row_masks.values():
            if mask == 0:
                ans += 2
            elif (mask & 5) == 0: 
                ans += 2
            elif (mask & 7) != 7:  
                ans += 1
                
        return ans