def karatsuba(x,y):
	
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5,ceil(n/2),1000_000_007) * pow(4,floor(n/2),1000_000_007))% 1000_000_007
        # 4 ! @ odd indexes
        # 5 ! @ even incexes
        mod=10**9 + 7
        half=n//2
        if n%2==0:           
                        
            return karatsuba(4**half,5**half)%mod
        else:            
            return (karatsuba(4**half,5**half) *5)%mod