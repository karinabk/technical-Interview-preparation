from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj=defaultdict(list)
        count = 0 
        given = set()
        for con in connections:
            adj[con[0]].append(con[1])
            adj[con[1]].append(con[0])
            given.add((con[0],con[1]))
        visited = [False] * n
       
        def backtraverse(val):
            
            visited[val] = True
            num = 0
            
            for road in adj[val]:
                if not visited[road]:
                    if (road,val) not in given:
                        num += 1
                    num += backtraverse(road)
            return num
        count += backtraverse(0)
        
        return count
            
        
        
