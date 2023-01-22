class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        d=collections.Counter(words[0])
        
        #unbiased collection
        
        for i in words:
            newd= collections.Counter(i)
            # print(i, newd)
            for k, v in d.items():                
                if k in newd:
                    d[k] = min(newd[k], v)
                else:
                    
                    d[k]=0
                    
        arr=[]
        for k, v in d.items():
            for i in range(v):
                arr.append(k)
        return arr
                    
        
        
                
            
        