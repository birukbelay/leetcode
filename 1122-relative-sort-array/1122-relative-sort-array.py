from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d= Counter(arr1)
        arr1.sort()
        
        ans=[]
        for i in arr2:
            for j in range(d[i]):
                ans.append(i)
            d.pop(i, None)
        for i in arr1:
            if i in d:
                ans.append(i)
        return ans
                
        