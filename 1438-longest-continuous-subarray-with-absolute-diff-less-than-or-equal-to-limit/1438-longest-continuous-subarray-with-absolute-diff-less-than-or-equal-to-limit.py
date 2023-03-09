from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=0
        
        inc=deque()
        dec=deque()
        maxVal=0
        for r in range(len(nums)):
            v=nums[r]
            while dec and v> nums[dec[-1]]:
                dec.pop()
            dec.append(r)
            
            while inc and v < nums[inc[-1]]:
                inc.pop()
            inc.append(r)
            
            maxI=dec[0]
            minI= inc[0]
            
            while l<len(nums) and nums[maxI]- nums[minI] > limit:
                l+=1
                
                while dec and dec[0]<l:
                    dec.popleft()
                while inc and inc[0]<l:
                    inc.popleft()
                maxI=dec[0]
                minI= inc[0]
            
            maxVal= max(maxVal, r-l+1)
        return maxVal