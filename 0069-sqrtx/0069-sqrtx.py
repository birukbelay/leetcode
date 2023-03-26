class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<=1:
            return x
        
        l,r=0,x//2
        
        if r**2==x:
            return r
        while l<=r:
            mid=(l+r)//2
            
            if mid**2>x:
                r=mid-1
            else:
                l=mid+1
        return l-1
            
            