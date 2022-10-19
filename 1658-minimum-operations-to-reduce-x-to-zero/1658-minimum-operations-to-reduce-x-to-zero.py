class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        Sum=sum(nums)
               
        N=len(nums)
        
        k=Sum-x 
        L=0
        curSum=0
        MAXL=0
        if k==0:
            return N
        for i in range(N):
            curSum+=nums[i]
            print(curSum)
            while curSum>=k and L<=i:
                
                if curSum==k:
                    MAXL=max(MAXL, i-L+1)
                curSum-=nums[L]
                L+=1
        print(MAXL)
        if MAXL<=0:
            return -1
        return N-MAXL
            
            
        