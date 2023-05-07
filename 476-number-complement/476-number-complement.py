class Solution:
    def findComplement(self, num: int) -> int:
        
        def toBinary(k):
            arr=[]
            while k>0:
                l=k%2                
                k//=2
                arr.append(l)
            l, r=0, len(arr)-1
            while l<r:
                arr[l], arr[r]=arr[r], arr[l]
                l+=1
                r-=1
            return arr
        
        def toDecimal(binArr):
            l=len(binArr)-1
            sum=0
            ctr=0
            for i in range(l,-1, -1):
                if binArr[i]==1:
                    sum+= 2**ctr
                ctr+=1
            return sum
        arr=toBinary(num)
        
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=1
            else:
                arr[i]=0
        return toDecimal(arr)