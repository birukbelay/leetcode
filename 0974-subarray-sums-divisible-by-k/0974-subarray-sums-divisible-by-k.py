class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        ctr, prefsum,d=0,0,{0:1}
        for i in nums:
            prefsum = (prefsum +i)%k
            ctr+=d.get(prefsum, 0)
            d[prefsum]=d.get(prefsum, 0) + 1
        return ctr
            