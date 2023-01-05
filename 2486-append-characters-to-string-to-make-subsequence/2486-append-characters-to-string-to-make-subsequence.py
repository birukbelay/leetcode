class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Approach: 
        # 1. find the maximum similarty bn s & t starting from t's 0 index
        # 2. keep a variable that track t's index from the first
        # t is the original -> s have to be like t
        if t in s:
            return 0
        tctr=0       
        
        for i in s:
            if i == t[tctr]:
                tctr+=1            
        return len(t)- tctr
        
        
        
        
        
            
                
            
        