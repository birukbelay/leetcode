class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=1+d.get(nums[i],0)
        ctr=0
        for key,v in d.items():
            if key+k in d:
                ctr+=d[key]*d[k+key]
        return ctr
            