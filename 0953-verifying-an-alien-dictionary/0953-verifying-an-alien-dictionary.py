class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i,v in enumerate(order):
            d[v]=i
        for i in range(1, len(words)):
            if not self.orders(d, words[i-1], words[i]):
                return False
                
        return True
    #make a function that compare the order of 2 words based on the alien order
    # return true if order of word 1 is smaller or equal to order of word 2
    def orders(self, d, word1, word2):
        l1,l2 =0,0
        
        while l1< len(word1) and l2< len(word2) and word1[l1] == word2[l2]:
            l1+=1
            l2+=1
        if l1 == len(word1):
            return True
        elif l2 == len(word2):
            return False
        else:
            return d[word1[l1]] < d[word2[l2]]
        
            
            

        