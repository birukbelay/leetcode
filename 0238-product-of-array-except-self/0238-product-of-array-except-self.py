class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix ,postfix=nums[:],nums[:]
        
        for i in range(1, len(nums)):
            prefix[i]*=prefix[i-1]
        for i in range(len(nums)-2, -1,-1):
            # print(i, nums[i])
            postfix[i]*=postfix[i+1]
        # print(postfix, prefix)
        
        for i in range(len(nums)):
            pre= prefix[i-1] if i>0 else 1
            post = postfix[i+1] if i<len(nums)-1 else 1
            nums[i]= pre * post
        return nums
        # simple soln
        
        # res=[1]*len(nums)
        # prefix=1
        # for i in range(len(nums)):
        #     res[i]=prefix
        #     prefix *= nums[i]
        # postfix=1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *=nums[i]
        # return res