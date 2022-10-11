class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        fin=""
        for i in s:
            d[i]= 1 + d.get(i,0)
        a=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in a.items():
            fin+= key*value
        print(fin)
        return fin
        