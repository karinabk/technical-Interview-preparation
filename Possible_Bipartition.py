from collections import defaultdict, deque
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for pair in dislikes:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            
        visited = dict()
        
        
        def dfs(pid,color):
            queue = deque()
            queue.append((pid,1))
            while queue:
                
                pid1, color = queue.pop()
                if pid1 in visited:
                    if visited[pid1] != color:
                        return False
                    continue
                visited[pid1] = color
                for n in graph[pid1]:
                    queue.appendleft((n,-color))
                    
            return True
                
            
        for pid in range(1,N+1):
            if pid not in visited:
                if not dfs(pid,1):
                    return False
            
        return True
            
       
