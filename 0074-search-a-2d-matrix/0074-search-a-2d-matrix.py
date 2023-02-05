class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        N = len(matrix) #3
        l=0
        while l<N and matrix[l][-1] < target:
            l+=1
        if l>=N:
            return False
        for i in range(len(matrix[0])):
            if matrix[l][i]== target:
                return True
        return False
            
        
#         end= len(matrix)
#         start= 0
#         mid= (end-start)//2
        
#         #some while loop here
#         while end>start:
#             if target> matrix[mid][-1]:
#                 start= mid+1
#                 mid=(end-start)//2
#             else:
#                 # look for the variable
#                 if target>= matrix[mid][0]:

#                     for i in matrix[mid]:
#                         if i==target:
#                             return True
#                     return False
#                 else:
#                     end=mid
#                     mid= (end-start)//2
                
                
                
        