class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
      
        def can_match_prefix(prefix_len):
            freq = s_counts.copy()
            for ch in target[:prefix_len]:
                if freq[ch] <= 0:
                    return False
                freq[ch] -= 1
            return True
        
        for i in range(n - 1, -1, -1):
            if not can_match_prefix(i):
                continue
            freq = s_counts.copy()
            for ch in target[:i]:
                freq[ch] -= 1
            pivot = None
            for ch in sorted(freq.keys()):
                if ch > target[i] and freq[ch] > 0:
                    pivot = ch
                    break
                    
            if pivot is not None:
                res = list(target[:i])
                res.append(pivot)
                freq[pivot] -= 1
                for ch in sorted(freq.keys()):
                    res.extend([ch] * freq[ch])
                    
                return "".join(res)
                
        return ""

        