class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        r=len(nums)-1
        l=0
        cnt=0
        path=0
        while r>=l:
            if nums[r]>nums[r-1]:
                
                cnt+=1
                cnt+=path
                r-=1
                path+=1
            else:
                path+=1
                r-=1
        return cnt