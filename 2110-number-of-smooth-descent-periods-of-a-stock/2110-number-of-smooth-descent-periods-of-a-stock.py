class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        L=len(prices)
        tot=L
        ctr=0
        for i in range(1,L):
            
            if prices[i]+1== prices[i-1]:
                ctr+=1
                tot+=ctr
            else:
                ctr=0
        return tot