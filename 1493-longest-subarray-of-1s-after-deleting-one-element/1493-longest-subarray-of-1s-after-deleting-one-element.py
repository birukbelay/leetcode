class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        tot=0
        l=0
        cnt=1
        lastZ=0
        for i in range(N):
            if nums[i]==0 and cnt<=0:
                l=lastZ+1
                lastZ=i
                
            elif nums[i]==0 and cnt>0:
                cnt-=1
                # print(i)
                lastZ=i
            # print(tot,"-", i,l)
            tot=max(tot, i-l)
        return tot
            