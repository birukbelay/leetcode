class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxVol=0 
        hieghtLen=len(height)
        while l<=r:            
            vol=min(height[r], height[l]) * (r-l)
            maxVol=max(maxVol, vol)
            if(height[r]>height[l]):
                l+=1
            else:
                r-=1
            
        # for i in range(hieghtLen):
        #     for j in range(i, hieghtLen):
        #         # print("i=", i, "h[i]=", height[i])
        #         # print("j=", j, "h[j]=", height[j])
        #         vol=min(height[i], height[j]) * (j-i)
        #         # print("len=", j-i, "vol=", vol)
        #         maxVol=max(maxVol, vol)
        return maxVol
#         
            
        
        