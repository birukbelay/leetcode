class Solution:
    def minSwaps(self, s: str) -> int:
        arr= [a for a in s]
        opning=[]
        ctr=0
        maxCtr=0
        for i in s:
            if i=='[':
                ctr-=1
            else:
                ctr+=1
            maxCtr=max(maxCtr, ctr)
        if maxCtr%2==1:
            return (maxCtr+1)//2
        return maxCtr//2