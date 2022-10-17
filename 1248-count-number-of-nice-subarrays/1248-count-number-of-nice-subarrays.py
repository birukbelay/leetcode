class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 0 if (nums[i]%2)==0 else 1
                       
        # sub array sum equals k problem
        d={0:1}        
        prefix=0
        # L=0
        ctr=0
        for i in range(len(nums)):
            prefix+=nums[i] 
            diff = prefix-k
            if diff in d:
                ctr+=d[diff]
            d[prefix]= d.get(prefix,0) +1
                

        return ctr
