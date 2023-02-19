class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # i=0
        def atMostK(k):
            d={}
            l=0
            ctr=0
            for i in range(len(nums)):

                d[nums[i]]= d.get(nums[i], 0)+1
                # if len(d)==k:
                #     ctr+=1
                while l<len(nums) and len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]<1:
                        d.pop(nums[l], None)
                    l+=1
                ctr+= i-l+1
            return ctr
        return atMostK(k) - atMostK(k-1)
        # 1 2 1 2 3     
        