class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        cur=0
        ctr=0
        L=0
        N=len(arr)
        for i in range(N):
            cur+=arr[i]
            if i>=k-1:
                avg=cur//k
                if avg>= threshold: ctr+=1
                cur-=arr[L]
                L+=1
        return ctr