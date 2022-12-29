class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N=len(nums)
        n=[0]*(N+1)
        duplicates=[]
        for i in nums:
            n[i]+=1
            if n[i]==2:
                duplicates.append(i)
        for i in range(1, N+1):
            if n[i]==0:
                duplicates.append(i)
        return duplicates


        
