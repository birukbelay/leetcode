class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=0
        maxAvg=- sys.maxsize
        l=0
        for i in range(len(nums)):
            
            sums+=nums[i]
            if i>=k-1:
                avg=sums/k
                maxAvg=max(maxAvg, avg)
                sums-=nums[l]
                l+=1
        return maxAvg
            
        