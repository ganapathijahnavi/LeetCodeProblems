class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        n = len(word)
        count = 0
        for i in range(n):
            curr_vowels = set()
            for j in range(i,n):
                char = word[j]
                if char not in vowels:
                    break
                curr_vowels.add(char)
                if len(curr_vowels) == 5:
                    count += 1
        return count
        