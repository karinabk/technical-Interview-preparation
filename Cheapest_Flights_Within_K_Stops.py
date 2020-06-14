from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        
        adj = defaultdict(dict)
        for flight in flights:
            adj[flight[0]][flight[1]] = flight[2]
        
        priority_queue = [(0,src, K+1)]
        while priority_queue:
            weight,start, k  = heappop(priority_queue)
            if start == dst:
                return weight
            if k:
                for adj_el in adj[start]:
                    heappush(priority_queue, (weight + adj[start][adj_el], adj_el,k  - 1))
        return -1
        
                    
        
