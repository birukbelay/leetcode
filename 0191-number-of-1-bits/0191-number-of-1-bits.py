class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr=0
        while n:
            if n% 2!=0:
                ctr+=1
            n = n>>1
        return ctr
        