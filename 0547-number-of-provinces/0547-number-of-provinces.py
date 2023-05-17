class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, m = len(isConnected), len(isConnected[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        seen = set()
        ctr=0
        def dfs(i):
            seen.add(i)
            for j in range(m):
                if isConnected[i][j]==1 and j not in seen:
                    dfs(j)
            
            
            
            
        for row in range(n):
            
            if row not in seen:
                
                dfs(row)
                ctr+=1
                    
        return ctr
                    
                    
                
            
        
        
        
        