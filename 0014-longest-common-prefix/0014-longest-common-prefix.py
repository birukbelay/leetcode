class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest= strs[0]
        for i in strs:
            if len(i)<len(smallest):
                smallest=i
        pre = ""
        ctr=0      
        
        for i in range(len(smallest)):        
            for j in strs:
                if j[i] != smallest[i]:
                    return pre
            pre+=smallest[i]
        return pre
                    
        
            
        