class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left_sum, left_q = 0, 0
        right_sum, right_q = 0, 0
    
        for char in num[:half]:
            if char == '?':
                left_q += 1
            else:
                left_sum += int(char)

        for char in num[half:]:
            if char == '?':
                right_q += 1
            else:
                right_sum += int(char)
                
        if (left_q + right_q) % 2 != 0:
            return True
            
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)
        