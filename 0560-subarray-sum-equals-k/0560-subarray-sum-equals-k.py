class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ctr , prefsum, d = 0,  0, {0:1}

        for n in nums:
            prefsum += n
            if  prefsum-k  in  d:
                ctr += d[prefsum-k]
            d[prefsum] = d.get(prefsum, 0) + 1
        return ctr