class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot=-sys.maxsize
        sums=0
        maxN=-sys.maxsize
        for i in range(len(nums)):
            
            if sums== -sys.maxsize:
                sums=nums[i]
            else:
                sums+=nums[i]            
            
            if sums<0:
                sums= -sys.maxsize
            tot=max(tot, sums)
            maxN=max(maxN, nums[i])
        if tot== -sys.maxsize:
            return maxN
        return tot
                   
        