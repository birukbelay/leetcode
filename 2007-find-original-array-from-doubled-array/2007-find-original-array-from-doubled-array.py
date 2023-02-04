class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        d={}
        arr=[]
        changed.sort()
        for i in range(len(changed)):
            val=changed[i]
            d[val]= d.get(val, 0) +1
            
        for j in range(len(changed)):
            k=changed[j]
                        
            #check d[k*2] exixt in the arr
            if d[k]>0 and  k*2 in d and d[k*2]>0:                
                d[k] -= 1
                d[k*2] -= 1
                if d[k] >= 0:                
                    arr.append(k)
        if len(arr)==len(changed)/2:
            return arr
        else:
            return [] 