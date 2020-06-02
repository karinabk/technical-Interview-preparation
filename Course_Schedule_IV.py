
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        table = [[False] * n for _ in range(n)]
        
        for i, j in prerequisites:
            table[i][j] = True
            
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    table[i][j] = table[i][j] or (table[i][k] and table[k][j])
            
        return [table[i][j] for i, j in queries]
        
        
