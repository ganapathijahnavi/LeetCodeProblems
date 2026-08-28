class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2
        freq = Counter(s)

        center = ""
        odd_count = 0
        for char, count in list(freq.items()):
            if count % 2 != 0:
                odd_count += 1
                center = char
                freq[char] -= 1
            freq[char] //= 2 
        if odd_count > 1:
            return ""

        def make_palindrome(head: str) -> str:
            tail = head[::-1]
            return head + center + tail

        def can_form(prefix: str) -> bool:
            temp = freq.copy()
            for ch in prefix:
                if temp[ch] <= 0:
                    return False
                temp[ch] -= 1
            return True

        target_head = target[:half]
        if can_form(target_head):
            candidate = make_palindrome(target_head)
            if candidate > target:
                return candidate

        for i in range(half - 1, -1, -1):
            prefix = target[:i]
            if not can_form(prefix):
                continue
                
            temp = freq.copy()
            for ch in prefix:
                temp[ch] -= 1
                
            for ch in sorted(temp.keys()):
                if ch > target[i] and temp[ch] > 0:
                    temp[ch] -= 1
                    rest = []
                    for k in sorted(temp.keys()):
                        rest.extend([k] * temp[k])
                        
                    head = prefix + ch + "".join(rest)
                    return make_palindrome(head)
                    
        return ""
        