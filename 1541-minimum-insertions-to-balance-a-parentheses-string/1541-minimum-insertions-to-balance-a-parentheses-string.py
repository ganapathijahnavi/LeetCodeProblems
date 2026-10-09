class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                st.append('(')
                i += 1
            else:
                if i + 1 < n and s[i+1] == ')':
                    i += 2
                else:
                    ans += 1 
                    i += 1
                if st:
                    st.pop()
                else:
                    ans += 1
        ans += 2 * len(st)
        return ans