class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr=[]
        def cal(k):
            ctr=0
            while k>0:
                l=k%2
                if l==1:
                    ctr+=1
                k//=2
            return ctr
        for i in range(n+1):
            arr.append(cal(i))
        return arr
                