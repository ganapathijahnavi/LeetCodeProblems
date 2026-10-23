class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        start = 0
        vowel_count = 1
        for i in range(1,len(word)):
            if word[i] < word[i-1]:
                start = i
                vowel_count = 1
            elif word[i] > word[i-1]:
                vowel_count += 1
            if vowel_count == 5:
                max_len = max(max_len, i - start + 1)
        return max_len

