class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        row= len(box)
        col= len(box[0])
        
        ans = [[0] * row for _ in range(col)]
        
        # print(row, col, box)
        for i in range(row):
            l= col-1
            for j in range(col-1, -1, -1):
                # print(j, j-1)
                # if l<j:
                # while l>0  and l!='.':                    
                #     l-=1
                # if box[i][j]="#":
                #     l-=1
                if box[i][j]=='*':                    
                    l=j-1
                if box[i][j]=='#':
                    # print(l,j)
                    box[i][j], box[i][l]= box[i][l], box[i][j]
                    l-=1
                
                #[#....###]
                
                        
        # print(box)
        
        for i in range(row):
            for j in range(col):
                ans[j][row-1-i]= box[i][j]
        return ans
        #[#..]
        