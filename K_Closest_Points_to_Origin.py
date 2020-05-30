from math import sqrt
from heapq import heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        minheap = []
        
        for point in points:
            heappush(minheap,(sqrt(point[0]**2 + point[1]**2), point[0],point[1]))
        result = []
        for _ in range(K):
            item = heappop(minheap)
            result.append([item[1], item[2]])
        
        return(result)
        
        
        
