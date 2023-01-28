class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=[0]*101
        
        for i in nums:
            n[i]+=1
        newarr=[]
        for i in range(len(n)):
            newarr +=  [i] * n[i]
        print(newarr)
        arr=[]
        for i in range(len(newarr)):
            if newarr[i]==target:
                arr.append(i)
        return arr
            