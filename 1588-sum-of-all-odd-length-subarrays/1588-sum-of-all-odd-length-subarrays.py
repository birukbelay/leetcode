class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tot = sum(arr)
        print(tot)
        for i in range(len(arr)):
            s = arr[i]
            for j in range(i+1, len(arr)):
                s += arr[j]
                if (j-i)%2 ==0:
                    tot+=s
                
        return tot
                
        
                