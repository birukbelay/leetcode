class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        
        tot=0
        
        l=r=-1
        # edge cases
            # the Subarry is subarray of numbers who are all below left and one number is abov right 
        
        for i in range(len(nums)):
            if nums[i]>=left:
                r=i
            if nums[i] >right:
                l=i
            tot+=r-l
        return tot
                
                
            
        
        