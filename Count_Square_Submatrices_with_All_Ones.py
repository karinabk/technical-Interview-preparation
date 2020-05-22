class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        memo = []
        memo.append(matrix[0])
        for i in range(1,len(matrix)):
            memo.append([matrix[i][0]]+[0]*(len(matrix[0])))
       
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 1:
                    memo[row][col] = min(memo[row-1][col],memo[row][col-1],memo[row-1][col-1]) + 1
        sum_ = 0
        for row in memo:
            for col in row:
                sum_ += col
        return(sum_)
        
