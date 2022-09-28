class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # l=0
        
        # create a dictionary
        # d={}
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        dc={}
        for i in range(len(nums)):
            
            r=nums[i]
            # if d[r] >1:                
            if r in dc:
                # d[r]-=1
                # while nums[l]!=r and l<=i:
                    # l+=1
                if i-dc[r]<=k:
                    return True
                else:
                    dc[r]=i
            else:
                dc[r]=i
        return False
                    
            