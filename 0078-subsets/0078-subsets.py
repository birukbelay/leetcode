class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = [[]]
        
        for i in nums:
            new = []
            for j in output:
                new.append(j + [i]  )            
            
            output += new
        
        return output
            
        
        
        
        
        
        
        # lst=[]
        # lst.append([])
        # for i in range(len(nums)):
        #     lst.append([nums[i]])
        #     for j in range( i):
        #         lst.append([nums[j],nums[i]])
        # return lst
            