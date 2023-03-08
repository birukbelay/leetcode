class Solution:#9min
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        empt=[0] *(2050-1950+1)
        
        for i in logs:
            b,d=i[0]-1950,i[1]-1950
            
            empt[b]+=1
            empt[d]-=1
        
        for i in range(1, len(empt)):
            empt[i]+= empt[i-1]
        
        maxI=0
        for i in range(len(empt)):
            if empt[i]> empt[maxI]:
                maxI=i
        return maxI+1950
            
            
        