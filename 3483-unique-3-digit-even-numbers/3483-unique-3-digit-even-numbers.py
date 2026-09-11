class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = Counter(digits)
        unique_valid_numbers = set()
        
        def build_number(current_digits):
            if len(current_digits) == 3:
                if current_digits[0] == 0:
                    return
                
                if current_digits[-1] % 2 != 0:
                    return
               
                num = current_digits[0] * 100 + current_digits[1] * 10 + current_digits[2]
                unique_valid_numbers.add(num)
                return
            
            for digit in digit_counts:
                if digit_counts[digit] > 0:
                    digit_counts[digit] -= 1
                    current_digits.append(digit)
                    
                    build_number(current_digits)
                    current_digits.pop()
                    digit_counts[digit] += 1
        build_number([])
        
        return len(unique_valid_numbers)

        