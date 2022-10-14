class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        # i,j,k=0,1,len(arr)-1
        arr.sort()
        n=len(arr)
        ctr=0
        for i in range(n-2):
            num1= arr[i]
            l,r=i+1, n-1
            t=target-num1
            
            while l<r:
                sums= n + arr[l] + arr[r]
                if arr[l]+arr[r]>t:
                    r-=1
                elif arr[l]+arr[r]<t:
                    l+=1
                elif arr[l] !=arr[r]:
                    cnt1=cnt2=1
                    while l +1 <r and arr[l] == arr[l+1]:
                        cnt1+=1
                        l+=1
                    while l <r-1 and arr[r] == arr[r-1]:
                        cnt2+=1
                        r-=1
                    ctr+=cnt1 *cnt2
                    l+=1
                    r-=1
                
                # we found valid tuple
                else:
                    length=r-l+1
                    ctr+=length * (length -1) //(2*1)
                    break
        mod = 10**9+7            
        # print(d, ctr)
        return ctr%mod

        
                