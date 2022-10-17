class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        # for i in range(1,len(self.nums)):
        #     self.nums[i]+=self.nums[i-1]
        # print(self.nums)
        return sum(self.nums[left:right+1] )

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)