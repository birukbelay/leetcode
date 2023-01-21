import collections
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #make an array with the power of 2's
        arr=[0]*22
        for i in range(22):
            arr[i] = 2**i
        #count the repetition of foods with same deliciousness 
        d = collections.Counter(deliciousness)
        tot=0
        #
        s=set(deliciousness)
        # print(s)
        # print(d)
        #set of deliciousness
        for i in deliciousness:
            d[i]-= 1
            for powr in arr:                
                k= d.get(powr-i, 0)
                tot+=k               
                
                    
        # for i in s:
        #     for powr in arr:
        #         if powr-i in d:
        #             if i==powr-i:
        #                 if d[i]>2:                            
        #                     tot+= d[i]                            
        #             else:
        #                 tot+= d[i] * d[powr-i]
        #     d.pop(i, None)
        return tot%(10**9 + 7)
        # [0,1]    
                    
                    
                    
                    
            
            
            
            
            

        
        
        
        
        
        