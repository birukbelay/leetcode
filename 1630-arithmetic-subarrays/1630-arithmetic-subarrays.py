class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        # brute force
        ans=[]
        for i in range(len(l)):
            fst= l[i]
            lst=r[i]
            newArr = nums[fst: lst+1]
            nl= len(newArr)
            if nl<2:
                ans.append(False)
                continue
            
            newArr.sort()
            ctr= newArr[1]-newArr[0]
            err=True
            for i in range(1, nl):
                if newArr[i]-newArr[i-1] !=ctr:
                    ans.append(False)
                    err=False
                    break
            if err:
                ans.append(True)
        return ans
                
        