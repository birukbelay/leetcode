class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        if len(arr)<=2: return 0

        tot=0      

        switch=-1
        
        for i in range(1,len(arr)-1):
            
            # find peak point
            if arr[i]> arr[i-1] and arr[i]> arr[i+1]:
                l=i
                ctr=0
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                r=i
                while r<len(arr)-1 and arr[r] > arr[r+1]:
                    r+=1
                tot=max(tot, r-l+1)
        return tot

            