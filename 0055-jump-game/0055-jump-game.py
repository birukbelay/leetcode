class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N=len(nums)
        maxN=nums[0]
        if N<2: return True
        for i in range(len(nums)):
            maxN= max(maxN,i+ nums[i])
            
            if i>=maxN:
                if i ==N-1: return True
                return False
        return True
