class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # [ (180, "mary"), (165, john), (170, Emma)]
        newArr=[]
        for i in range(len(names)):
            newArr.append((heights[i], names[i]))
            
        newArr.sort(reverse=True)
        # print(newArr)
        ans=[]
        for i in newArr:
            ans.append(i[1])
        return ans
        
            
            
        
        