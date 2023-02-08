class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArr=nums1[:]
        
        n1,n2=0,0
        ctr=0
        while ctr< n+m:
            if n1<m and n2<n:
                if newArr[n1]<nums2[n2]:
                    nums1[ctr]=newArr[n1]
                    n1+=1
                else:
                    nums1[ctr]=nums2[n2]
                    n2+=1
            else:
                dif1= m-n1
                dif2= n-n2
                if dif1==0:
                    nums1[ctr]=nums2[n2]
                    n2+=1                    
                elif dif2==0:
                    nums1[ctr]=newArr[n1]
                    n1+=1                
            ctr+=1
            
            
            
        
        
        