class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def subsets(indx, out):
            if len(out) == k:
                res.append(out[:])
                return
            for i in range(indx, n + 1):
                out.append(i)
                subsets(i+1, out)
                out.pop()
            return res
        return subsets(1,[])
        