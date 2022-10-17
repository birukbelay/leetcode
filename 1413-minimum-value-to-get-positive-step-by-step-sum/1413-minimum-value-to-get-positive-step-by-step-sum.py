class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal=nums[0]
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
            minVal=min(minVal, nums[i])
        if minVal>=0: return 1
        return abs(minVal)+1
            