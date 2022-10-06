class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k% len(nums)
        L=len(nums)-1
        self.reverse(nums, 0, L)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, L)
    def reverse(self, arr, l, r):
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l,r = l+1, r-1
        
        
        
        
        # nums = nums[k+1:len(nums)] + nums[:k+1]
        
        # return nums[k+1:len(nums)] + nums[:k+1]