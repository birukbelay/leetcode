class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        # tot=1
        # for i in range(abs(n)):
        #     tot*=x
        # if n<0:
        #     return 1/tot
        # elif n==0:
        #     return 1
        # return tot
        

        
        
        return self.xpow(x, n, x, abs(n))
    def xpow(self, x:float, n:int, tot:float, ctrN:int):
        if n==0:
            return 1
        if ctrN==1:
            if n<0:
                return 1/tot
            return tot
        if ctrN%2==0:
            return self.xpow(x*x, n, tot*x, ctrN/2)
        # print("x-",x, "n-",n)
        return self.xpow(x, n, tot*x, ctrN-1)
        
        