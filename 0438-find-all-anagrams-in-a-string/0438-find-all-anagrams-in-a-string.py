class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N=len(s)
        ctr=0
        d={}
        dctr={}
        output=[]
        l=0
        for i in p:
            d[i]= d.get(i,0)+1
        
        for i in range(N):
            if s[i] in d:
                dctr[s[i]]= dctr.get(s[i],0)+1
                # print(i, s[i])
                # print(dctr,"--", d)
                if dctr[s[i]]<= d[s[i]]:
                    # print(i, s[i])
                    ctr+=1
            if ctr==len(p):
                output.append(l)
            
            if i >= len(p)-1:
                L=s[l]
                if L in dctr and dctr[L]>0:
                    dctr[L]-=1
                    # if it was d[L] +1, it would be equal and wont get into this condition
                    if dctr[L] <d[L]:
                        ctr-=1
                l+=1
        return output