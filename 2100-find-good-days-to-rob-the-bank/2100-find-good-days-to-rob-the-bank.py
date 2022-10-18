class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        L=len(security)
        dec=[0]*L
        inc=[0]*L
        goodDays=[]
        # decreasing array
        for i in range(1,L):            
            if security[i]<=security[i-1]:
                dec[i]=dec[i-1]
            else:
                dec[i]=i
        # print(dec)
        # increasing arr
        for i in range(L-1, -1, -1):
            
            if i == L-1:
                inc[i]=i
            elif security[i]<=security[i+1]:
                inc[i]=inc[i+1]
            else:
                inc[i]=i
        
        for i in range(L):
            if i>=time and i< L-time:
                # 1. check if currentIndex - decreasingStartingPt >=time
                # 2. if increasingStartPoint to the right -curIndex >= time
                if i-dec[i] >=time and inc[i]-i >=time:
                    goodDays.append(i)
        return goodDays
        