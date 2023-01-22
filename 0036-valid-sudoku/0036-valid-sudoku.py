class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row= len(board)
        col= len(board[0])
        
        d={}        
        
        #validate rows
        for i in range(row):
            
            for j in range(col):
                if board[i][j] in d:
                    print(d)
                    print(board[i][j])
                    print("invalid row")
                    return False
                else:
                    val=board[i][j]
                    if val!=".":
                        d[val]=1
            d={}
        
        #validate cols
        for i in range(col):
            for j in range(row):
                
                if board[j][i] in d:
                    print(d)
                    print("invalid Col")
                    return False
                else:
                    
                    val=board[j][i]
                    if val!=".":
                        d[val]=1
            d={}
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                m=self.checkMini(board, i,j)
                if not m:
                    return False
        return True
        


        
        
    def checkMini(self,board, row,col):
        d={}
        for i in range(3):
            for j in range(3):
                r= i+row
                c= j+col
                if board[r][c] in d:
                    print("invalid mini")
                    return False
                else:
                    val=board[r][c]
                    if val!=".":
                        d[val]=1
                    
        return True

                
                
        