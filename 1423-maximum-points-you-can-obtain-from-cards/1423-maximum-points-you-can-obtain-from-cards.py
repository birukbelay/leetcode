class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        #to find sum of all the cards
        s=sum(cardPoints)
        N=len(cardPoints)
        if k==N: return s
        # a window of len of nums - k
        sub=N-k
        
        L=0
        temp=0
        tot=sys.maxsize
        # to find a window of N-k with minimum sum
        for i in range(N):
            temp+=cardPoints[i]

            
            if i>=sub-1:
                
                tot=min(tot, temp)
                
                temp-=cardPoints[L]
                L+=1
        
        return s-tot
            