class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l,r=0, len(nums)-1
        
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            otr= target-nums[i]
            if otr in d and d[otr]!=i:
                return [i, d[otr]]
                
            
        return []


        