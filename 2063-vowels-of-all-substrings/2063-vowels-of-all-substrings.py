class Solution:
    def countVowels(self, word: str) -> int:
        ctr=0        
        L=len(word)
        for i,v in enumerate(word):                     
            if v in "aeiou":
                ctr+=(i+1) * (L-i)        
        return ctr