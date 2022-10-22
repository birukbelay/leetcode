class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d={"a","e","i","o","u"}
        l=0
        ctr=0
        tot=0
        N=len(s)
        for i in range(N):
            if s[i] in d:
                ctr+=1
            if i>=k-1:
                tot=max(tot, ctr)
                if s[l] in d:
                    ctr-=1
                l+=1
        return tot
                