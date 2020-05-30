from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def isCycle(val,adj):
            if visited[val]:
                return True
            visited[val] = True

            for el in adj[val]:
                if isCycle(el,adj):
                    return True
            visited[val] = False
            return False
            
        adj = defaultdict(list)
        
        for course in prerequisites:
            adj[course[0]].append(course[1])
            adj[course[1]]
            
        for key in adj.keys():
            visited = [False] * numCourses
            if isCycle(key, adj):
                return False
        return True
            
                
