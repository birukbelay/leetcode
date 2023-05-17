class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        
        
#         old_color = image[sr][sc]
#         if color == old_color:
#             return image
        
#         n,m = len(image), len(image[0])
#         def dfs(i,j):
            
#             image[i][j] = color

#             for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:

#                 ni = i + di
#                 nj = j + dj


#                 in_bound = 0 <= ni < n and 0 <= nj < m

#                 if in_bound and image[ni][nj] == old_color:
#                     dfs(ni,nj)
        
#         dfs(sr,sc)
#         return image
    
    
        
        
        n, m = len(image), len(image[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # def in_bound(row, col):
        #     return 0 <= row < r and 0 <= col < c
        
        # seen = set()
        val= image[sr][sc]
        
        if val == color:
            return image
        
        def dfs(i, j):
            image[i][j]=color
            # seen.add((rw, cl))
            
            # print(rw, cl)
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                
                in_bound = 0 <= nr < n and 0 <= nc < m
                if in_bound and image[nr][nc] ==val:
                    dfs(nr, nc)
                
                # if (nr, nc) not in seen:                    
                
        dfs(sr, sc)
        return image
        
        
        