class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        subset=[]
        def dfs(i):
            if i>=len(nums):
                result.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+ 1)
            
            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result
        
        
        
        
        
        
        
        
        
        
        
        output = [[]]
        
        for i in nums:
            new = []
            for j in output:
                new.append(j + [i])
            output += new
        
        return output
            
        
        
        
        
        
        
        # lst=[]
        # lst.append([])
        # for i in range(len(nums)):
        #     lst.append([nums[i]])
        #     for j in range( i):
        #         lst.append([nums[j],nums[i]])
        # return lst
            