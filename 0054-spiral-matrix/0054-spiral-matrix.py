class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        newArr=[]
        leftBoundary=0       
        
        rightBoundary =len(matrix[0])
        bottomB=len(matrix)       
        topB=0
        
        retLen= bottomB *rightBoundary
        
        while leftBoundary<rightBoundary and topB<bottomB:
            
            if retLen == len(newArr): return newArr
            # going right   
            rctr=topB
            while rctr<rightBoundary:
                newArr.append(matrix[topB][rctr])
                rctr+=1
            topB+=1
            # print("r-", newArr)
            
            if retLen == len(newArr): return newArr
            # going down
            topDownCtr =topB          
            while topDownCtr < bottomB:
                newArr.append(matrix[topDownCtr][rightBoundary-1])
                topDownCtr+=1
            rightBoundary-=1
            # print("d--", newArr)
            # going back/left 
            if retLen == len(newArr): return newArr
            backCtr= rightBoundary-1
            # print(backCtr,leftBoundary)
            while backCtr >=leftBoundary:
                newArr.append(matrix[bottomB-1][backCtr])
                backCtr -=1
            bottomB -=1
            # print("b--",newArr)
            # going up
            if retLen == len(newArr): return newArr
            upCtr= bottomB-1            
            while upCtr >= topB:
                # print(leftBoundary, upCtr)
                newArr.append(matrix[upCtr][leftBoundary])
                upCtr -=1
            leftBoundary +=1
            # print(newArr)
        return newArr
            
            
                
                
                
            
        
        