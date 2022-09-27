class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        d={}
        good=0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
            if i-l>=2:                
                if len(d) >2:                    
                    good+=1
                d[s[l]]-=1
                if d[s[l]]<=0:
                    d.pop(s[l], None)
                l+=1
            
        return good
                