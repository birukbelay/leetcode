class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        newArr=[0]*len(spells)
        potions.sort()
        # print("---->",potions)
        for i,v in enumerate(spells):
            # print("``````````````````````````````````````````````",i)
            # we find index of number which is greater than point
            point= success/v
            
            c= self.binaryS(potions, point)
            cp= c-1 if c==len(potions) else c
            # print("----->",i, v,"pt:",point, "c=",c, "arr[c]-", potions[cp])
            newArr[i]= len(potions)-c
        return newArr
    def binaryS(self,arr, pt):
        if pt>arr[-1]: return len(arr)
        if pt<arr[0]: return 0
            
        l,r=0, len(arr)
        # print("--------------------[",pt)
        mid= (l+r)//2
        while l<r:
            
            mid= (l+r)//2
            # print(l,r, "mid:",mid, arr[mid])
            if arr[mid]==pt:
                if arr[mid-1]<pt:
                    return mid
                # to find the first occurence of the point
                else:r=mid
            elif arr[mid]>pt:
                if arr[mid-1]<pt: return mid
                r=mid-1
            elif arr[mid]<pt:
                l=mid+1
        
        mid= (l+r)//2
        
        # print("returning mid--", mid)
        return mid
            