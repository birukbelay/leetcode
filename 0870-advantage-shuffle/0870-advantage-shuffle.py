class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        nums3=sorted(nums2, reverse=True)
        nums1.sort( reverse=True)
        N=len(nums1)
        l1, l3, r1, r3 = 0,0, N-1, N-1
        # print(nums3)
        while l1<=r1:
            if nums1[l1]>nums3[l3]:
                dval=d.get(nums3[l3], [])
                dval.append(nums1[l1])
                # print("dval",dval)
                d[nums3[l3]]= dval
                l3+=1
                l1+=1
            else:
                dval=d.get(nums3[l3], [])
                dval.append(nums1[r1])
                d[nums3[l3]]= dval
                l3+=1
                r1-=1
        newArr=[0]*N
        for i, v in enumerate(nums2):
            newArr[i]= d[v].pop()
        # print(d)
        return newArr