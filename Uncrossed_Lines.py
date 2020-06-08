class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    
        memo = [[0]*(len(B)+1) for _ in range((len(A)+1))]
        
        for a in range(1,len(A)+1):
            
            for b in range(1,len(B)+1):
                
                memo[a][b] = max(memo[a-1][b-1]+(A[a-1]==B[b-1]),memo[a-1][b],memo[a][b-1])
        return memo[-1][-1]
