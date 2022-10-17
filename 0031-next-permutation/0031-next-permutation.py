class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        
        p2,p1= len(nums)-1, len(nums)-2
        
        while p1>=0 and nums[p1+1] <=nums[p1]:
            p1-=1
        if p1>=0:
            while nums[p2]<=nums[p1]:
                p2-=1
            nums[p2],nums[p1]=nums[p1], nums[p2]
        self.reverse(nums, p1+1)
        
        # if r<0:
        #     self.reverse(nums, 0)
            
    def reverse(self, arr, start):
        i=start
        r=len(arr)-1
        
        while i<r:
            arr[i],arr[r]=arr[r],arr[i]
            r-=1
            i+=1
        