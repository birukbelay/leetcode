class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL=0
        ctr=0
        for i in nums:            
            if i==1:
                ctr+=1                
            else:                
                ctr=0
            maxL=max(ctr, maxL)
        return maxL
                
                
        