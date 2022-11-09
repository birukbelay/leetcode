class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        Nned=len(needle)
        N=len(haystack)
        n=0
        for i,v in enumerate(haystack):
            
            if N-i >= Nned:
                if needle == haystack[i:i+Nned]:
                    return i
        return -1