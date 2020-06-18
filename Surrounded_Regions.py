class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def mark(row,col):

            board[row][col] = '1'
            if row > 0 and board[row-1][col] == 'O':
                mark(row-1,col)
            if col > 0 and board[row][col -1] == 'O':
                mark(row,col-1)
            if row < len(board)-1  and board[row+1][col] == 'O':
                mark(row+1,col) 
            if col < len(board[0])-1 and board[row][col+1] == 'O':
                mark(row,col+1) 

        for col in range(len(board[0])):
            if board[0][col] =='O':
                mark(0,col)
            if board[-1][col] == 'O':
                mark(len(board)-1,col)
        for row in range(len(board)):
            if board[row][0] == 'O':
                mark(row,0)
            if board[row][-1] == 'O':
                mark(row,len(board[0])-1)

            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '1':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                
                
