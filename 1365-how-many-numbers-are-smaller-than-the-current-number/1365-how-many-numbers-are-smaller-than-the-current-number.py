class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # n= len(nums)
        # arr=[None] * n
        # for i in range(n):
        #     cnt=0
        #     for j in range(n):
        #         if nums[j]< nums[i]:
        #             cnt=cnt+1
        #     arr[i]=cnt
        #     # print("a->", arr)
        # return arr
    
        dArr=[0] *101
        for i in nums:
            dArr[i]+=1
        pArr= dArr[:]
        for i in range(1, len(pArr)):
            pArr[i] += pArr[i-1]
        
        ans=[]
        for i in nums:
            ans.append(pArr[i]-dArr[i])
        return ans
            
        
        
        