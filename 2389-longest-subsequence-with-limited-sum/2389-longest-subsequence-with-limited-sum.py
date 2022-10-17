class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        d={}
        ret=[0]*len(queries)
        
        for i in range(1, len(nums)):
            nums[i]+= nums[i-1]
        # print(nums)
        # for i in range(len(nums)):
        #     d[nums[i]]=i
        for i in range(len(queries)):
            print("-",i)
            for j in  range(len(nums)):
                if nums[j]>queries[i]:
                    # print(j,nums[j])
                    ret[i]=j
                    break
                ret[i]=j+1
        return ret