class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapArr=[]
        ctr=0
        for i in matrix:
            for j in i:
                if ctr>=k:                                            
                    heapq.heappush(heapArr, -j) 
                    heapq.heappop(heapArr)
                else:
                    heapq.heappush(heapArr,-j)
                ctr+=1
                    

                
        return -heapArr[0]
        
        
        
        