import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
        unavailable = []
        
        ans = [0] * len(tasks)
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            current_time = max(current_time, j)
            if not available and unavailable[0][0] > current_time:
                current_time = unavailable[0][0]
            while unavailable and unavailable[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, idx))
            
            weight, idx = heapq.heappop(available)
            ans[j] = idx
        
            heapq.heappush(unavailable, (current_time + task_time, weight, idx))
            
        return ans