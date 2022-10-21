class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad= [],[]
        def kSum(k, start, target):
            if k!=2:
                for i in range(start, len(nums) -k +1):
                    # if the number is duplicated
                    if i> start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            # base case, two sum II
            l,r= start, len(nums)-1
            
            while l<r:
                if nums[l] + nums[r]< target:
                    l+=1
                elif nums[l] + nums[r]> target:
                    r-=1
                else: 
                    res.append(quad + [nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        kSum(4, 0, target)
        return res
                
            
        # N=len(nums)
        # arr=set()
        # for a in range(N):
        #     for b in range(N):
        #         c,d= b+1, N-1
        #         while c<d:
        #             s=nums[a] +nums[b]+ nums[c] +nums[d]
        #             if s> target:
        #                 d-=1
        #             elif s<target:
        #                 c+=1
        #             else:
        #                 arr.add((nums[a], nums[b], nums[c], nums[d]))
        # return arr
                        

                        
                            
                        
                            
        