class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        hash_map = {}
        l = 0
        max_sum = 0
        for r in range(0,len(fruits)):
            hash_map[fruits[r]] = hash_map.get(fruits[r],0) + 1
            while len(hash_map) > 2 :
                hash_map[fruits[l]] -= 1
                if hash_map[fruits[l]] == 0:
                    del hash_map[fruits[l]]
                        
                l += 1
            max_sum = max(max_sum, r-l+1)
        return max_sum

        