class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        
        
            
        N1=len(word1)
        N2 = len(word2)
        l1,l2=0,0
        ans=""
        while l1<N1 and l2<N2:
            c1=word1[l1]
            c2=word2[l2]
            
            w1=word1[l1:]
            w2=word2[l2:]

            
            if w1>w2:
                ans+=c1
                l1+=1
            else:                    
                ans+=c2
                l2+=1

        if l1<N1 :
            ans+=word1[l1:]
        if l2<N2:
            ans+=word2[l2:]
        return ans
            
        
        
        
        
        
        
        #test cases that failed
        """
        "guguuuuuuuuuuuuuuguguuuuguug"
        "gguggggggguuggguugggggg"
        "jvjjjjjjvjjvjvjjjvjvjjjj"
        "jjjjjjvjjjjjjvjjjjv"
        "nngnnnbnttnngsnnntnbgnnnn"
        "nnnnnnnnnnnnnntn"
        "olnllnxlxllllllllllnlelllex"
        "oooooooooooooooooo"
        """