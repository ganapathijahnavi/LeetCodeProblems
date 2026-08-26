class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        left = 0
        min_cnt = 0
        for right in range(n):
            if s[right] == '1':
                min_cnt += 1
            while min_cnt == k:
                curr_str = s[left:right+1]
                if not ans or len(curr_str) < len(ans) or len(curr_str) ==len(ans) and curr_str < ans:
                    ans = curr_str
                if s[left] == '1':
                        min_cnt -= 1
                left += 1
        return ans