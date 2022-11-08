class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen=0
        d={}
        N=len(nums)
        ctr=0
        for i in range(N):
            if nums[i]==0:
                ctr-=1
            else:
                ctr+=1
            if ctr==0:
                maxLen= i+1
            if ctr in d:
                maxLen=max(maxLen, i-d[ctr])
            else:
                d[ctr]=i
        print(d)
        return maxLen
                
                