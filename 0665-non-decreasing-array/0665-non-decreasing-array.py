class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        tolerance=1
        N=len(nums)
        maxN=nums[0]
        for i in range(1, N):
            if nums[i]<nums[i-1]:
                
                if tolerance<1:
                    return False                    
                tolerance-=1
                if i>=2 and nums[i-2]>nums[i]:
                    print("less",i)
                    nums[i]=nums[i-1]  
                    
            
        return True
        # cnt_violations=0        
        # for i in range(1, len(nums)):                       
        #     if nums[i]<nums[i-1]:
        #         if cnt_violations==1:
        #             return False
        #         cnt_violations+=1
        #         if i>=2 and nums[i-2]>nums[i]:
        #             nums[i]=nums[i-1]                       
        # return True