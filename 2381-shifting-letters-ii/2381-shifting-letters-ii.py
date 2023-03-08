class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        empty=[0]* len(s)
        newS=""
        for i in shifts:
            l,r,d= i[0],i[1],i[2]
            if d==0: d=-1
                            
            empty[l]+=d
            if r<len(s)-1:
                empty[r+1]-=d                
        
        for i in range(1, len(empty)):
            empty[i]+=empty[i-1]
            
        # find encrypted value of char
        def CesarsValue(c, key):
            val = (ord(c)-97 +key)%26
            if val>=0:                
                return chr(97+val)
            else:
                
                return chr(97+val+26)
        
        for i in range(len(s)):
            newS+= CesarsValue(s[i], empty[i])
        return newS
        
        
        
        
            
        