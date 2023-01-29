class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
                
        dirc = [(0,1),(0,-1),  (1,0), (-1,0),    (1,1), (-1,-1), (-1,1), (1,-1) ]
        qset=set()
        
        for i  in queens:
            qset.add( (i[0], i[1]) )
        def inbound(r, c):
            if r>=0 and r<8 and c>=0 and c<8:
                return True
            return False
        
         
        def move(d):
            
            nxtCell= [ king[0]+d[0], king[1]+d[1] ]
            
            
            while inbound(nxtCell[0], nxtCell[1]):
                if (nxtCell[0], nxtCell[1]) in qset:
                    return nxtCell
                nxtCell[0]+= d[0]
                nxtCell[1]+= d[1]
                
                      
                
            return [-1,-1]
          
                
                  
        ans=[]             
        for i in dirc:
            val = move(i)
            if val!=[-1,-1]:
                ans.append(val)
        return ans
                      
                      
            
            
#         lst=[]
#         for q in queens:
            
#             if q[0]==king[0] or q[1]==king[1]:                
#                 lst.append(q)
#             elif q[0]-king[0]==q[1]-king[1]:
#                 lst.append(q)
#         return lst
            
        