class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m= len(grid), len(grid[0])
        in_bound=lambda row, col:0<=row<n and 0<=col<m
        DIR=[[0,1],[1,0],[-1,0], [0,-1]]
        
        visited=set()
#         help us iterate the grids in order

        minuteCtr=0
        
        rottenQueue=deque()
        freshQueue=deque()
        freshCtr=0
        
        #         finding all the rotten and fresh tomatoes
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rottenQueue.append((i,j,0))
                elif grid[i][j]==1:
                    freshCtr+=1                                        

        while rottenQueue:
            current=rottenQueue.popleft()
            for i in DIR:
                ptx=current[0] + i[0]
                pty=current[1] +i[1]
                minute=current[2]
                
                minuteCtr=max(minute, minuteCtr)
                
                if in_bound(ptx, pty) and (ptx, pty) and grid[ptx][pty]==1:
                    grid[ptx][pty]=2 #to mark the visited cells
                    rottenQueue.append((ptx,pty,minute+1))
                    # print( minute)
                    
                    print(freshCtr)
                    freshCtr-=1
        if freshCtr>0:
            print(freshCtr)
            return -1
        else:
            # print("min",minuteCtr)
            return minuteCtr
        