class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_hdif = 0
        max_wdif = 0
        horizontalCuts += [0, h]
        verticalCuts += [0, w]
        horizontalCuts.sort()
        verticalCuts.sort()
        
        for i in range(1,len(horizontalCuts)):
            max_hdif = max(max_hdif, abs(horizontalCuts[i-1]-horizontalCuts[i]))
        for i in range(1,len(verticalCuts)):
            max_wdif = max(max_wdif, abs(verticalCuts[i-1]-verticalCuts[i]))
        return (max_hdif*max_wdif)%(10**9 + 7)
            
            
            
            
        
          
            
        
            
        
