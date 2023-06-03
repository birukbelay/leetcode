class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        for i,j in roads:
            d[i].append(j)
            d[j].append(i)
        arr= sorted(d.items(), key=lambda item: len(item[1]), reverse=True)
        if len(arr)<1:
            return 0
        sums= len(arr[0][1]) + len(arr[1][1])
        print(arr)
        maxN=len(arr[0][1])
        cnt=0
        max1=[]
        max2=[]
        #find max 
        for key, ar in arr:
            if len(ar)==maxN and cnt==0:
                max1.append((key, ar))
                
            elif cnt ==0:
                cnt+=1                
                maxN=len(ar)
                
            if len(ar)==maxN and cnt!=0:
                max2.append((key, ar))
        
        
        # print(max1, max2)
        # find 2 arrays which are not connected
        if len(max1)>1:
            # print(1,"--",max1)
            for i in range(len(max1)):
                for j in range(i+1, len(max1)):
                    if max1[i][0] not in max1[j][1]:
                        return sums
            return sums-1
        elif len(max1)==len(max2):
            if arr[0][0] in arr[1][1]:
                return sums-1
            return sums
        else:
            for k, ar in max2:
                if arr[0][0] not in ar:
                    return sums
            return sums-1
                
                        
        
        