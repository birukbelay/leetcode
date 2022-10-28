class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        tot=0
        cnt={}
        for i in ages:
            cnt[i]= cnt.get(i,0) +1
        
        for a in cnt:
            for b in cnt:
                if self.valid(a,b):
                    
                    tot+= (cnt[a] * cnt[b])
                    if a==b: tot-=cnt[a]
        return tot
                    
        
    def valid(self, x,y):
        
        if y<= (0.5*x) +7 or y>x or (y>100 and x<100):
            
            return False
        else:
            
            return True