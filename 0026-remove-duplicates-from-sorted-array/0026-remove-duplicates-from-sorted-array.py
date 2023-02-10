class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N=len(nums)
        
        l=0
        i=1
        if N==1:
            # print("here")
            return 1
        while i  <N:
            
            while i< N and nums[i]==nums[l]:
                i+=1
            if i<N:
                nums[l+1]= nums[i]
            l+=1
        # k=l-1
        # print(nums[:l])
        # nums = nums[:l]
        return l
        
                
            

        
                
