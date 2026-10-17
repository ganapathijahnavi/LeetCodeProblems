class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        hash_map = {}
        res = 0
        n = len(nums)
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        indexed_nums = [(nums[i], digit_sum(nums[i]), i) for i in range(n)]
        indexed_nums.sort(key=lambda x: (x[1], x[0]))
        visited = [False] * n
        swaps = 0
        count = 0
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
                
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps