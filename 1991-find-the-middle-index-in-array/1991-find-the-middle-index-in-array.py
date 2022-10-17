class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        N=len(nums)
        newNums=nums[:]
#         tot=sum(nums)
#         cur=0
#         for i in range(N):
#             cur+=nums[i]
#             # print(tot, cur, nums[i])
#             if tot- cur== cur-nums[i]: ## ie. nums[i-1]: in prefix
#                 return i
#             # if i==len(nums)-1 and nums[i-1]==0: return i
#         return -1
#     --------- old code
        for i in range(1, N):
            nums[i]+=nums[i-1]
        # print(nums, newNums)
        for i in range(N):
            # print(nums[i], newNums[i])
            if nums[N-1]- nums[i]==nums[i]-newNums[i]:
                return i
        return -1
        