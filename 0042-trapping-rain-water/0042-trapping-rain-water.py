class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l,r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        tot=0
        
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax, height[l])
                tot+= lmax - height[l]
            else:
                r-=1
                rmax=max(rmax, height[r])
                tot+=rmax-height[r]
        return tot
        