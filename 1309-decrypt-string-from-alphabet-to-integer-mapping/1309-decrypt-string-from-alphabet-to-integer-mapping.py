class Solution:
    def freqAlphabets(self, s: str) -> str:
        sl = s.split("#")
        # print(sl)
        s=""
        d={}
        for i in range(1, 27):
            d[str(i)]=chr(96+i)
        # print(d)        
        for k in range(len(sl)-1):
            i=sl[k]
            if len(i)==2:
                s+= d[i]
            else:
                for j in range(len(i)-2):
                    s+=d[i[j]]
                s+=d[i[-2:]]
                
        if s[-1]=="#":
            i=sl[-1]
            if len(i)==2:
                s+= d[i]
            else:
                for j in range(len(i)-2):
                    s+=d[i[j]]
                s+=d[i[-2:]]
        else:
            for i in sl[-1]:
                s+= d[i]

        return s
                
                    
                    
                    

        