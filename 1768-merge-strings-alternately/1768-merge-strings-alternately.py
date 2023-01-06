class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        N1=len(word1)
        N2= len(word2)
        s=""
        for i in range(min(N1,N2)):
            s+= (word1[i] + word2[i])
        if N1>N2:
            return s+word1[N2:]
        elif N2>N1:
            return s+ word2[N1:]
        else:
            return s