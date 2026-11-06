class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda item: item[1])
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_servers = {}
        
        l = 0
        r = 0
        m = len(logs)
        
        for q_idx, q_val in indexed_queries:
            window_start = q_val - x
            window_end = q_val
            while r < m and logs[r][1] <= window_end:
                server_id = logs[r][0]
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                r += 1
         
            while l < m and logs[l][1] < window_start:
                server_id = logs[l][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                l += 1
                
            ans[q_idx] = n - len(active_servers)
            
        return ans