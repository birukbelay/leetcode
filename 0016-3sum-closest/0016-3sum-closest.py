class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N=len(nums)
        closer=sum(nums[:3])
        
        for a in range(N):
            b,c = a+1, N-1
            
            while b<c:
                s=nums[a] + nums[b]+ nums[c]
                print(s)
                if abs(target-s) < abs(target-closer): closer=s
                
                if s>target:
                    c-=1
                elif s<target:
                    b+=1
                else:
                    return s
                
        return closer