class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d={}
        for i in sentence:
            # dfor i in sentence:
            d[ord(i)]=1
        return len(d)==26