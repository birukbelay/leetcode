class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # if k <= 1: return 0
        # prod = 1
        # ans = left = 0
        # for right, val in enumerate(nums):
            # prod *= val
            # while prod >= k:
                # prod /= nums[left]
                # left += 1
            # ans += right - left + 1
        # return ans
        
        if k <= 1: return 0
        l=0
        cnt=0
        prod=1
        
        for i in range(len(nums)):
            prod *=nums[i]
            # cnt+=1
            
            while prod >= k:
                
                prod /=nums[l]
                l+=1
            cnt += i-l + 1
        return cnt