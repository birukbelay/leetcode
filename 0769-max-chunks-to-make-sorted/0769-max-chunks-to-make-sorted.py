class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        l=0
        chunk=0
        bigArr=[0]
        for i in range(1,len(arr)):
            # print(arr[bigArr[i-1]], arr[i])
            if arr[bigArr[i-1]]> arr[i]:
                # print("here")
                bigArr.append(bigArr[i-1])
            else:
                bigArr.append(i)
        # print(bigArr)    
        minIdx=0
        
        maxIdx=0
        lastIdx=-1
        
        tempB=0
        # minVal=arr[0]
        while l< len(arr):
            # find the min num so far
            for i in range(l, len(arr)):
                if arr[i]<arr[minIdx]:
                    minIdx=i
                
                    
            # find biggest num until min num
            for i in range(l, minIdx+1):
                if arr[i]>arr[maxIdx]:
                    maxIdx=i
            # ----------------- this is where it gets hard        
            # ss=minIdx+1
            # found=True
            # while ss< len(arr) and found:
            #     if arr[ss]<arr[maxIdx]:
            #         lastIdx=ss
            #     if arr[ss]> arr[maxIdx]:
                    
            # find the last smaller than maxIdx
            for i in range(minIdx+1, len(arr)):
                if arr[i]< arr[maxIdx]:
                    # print("here", i, arr[i])
                    # print(bigArr)
                    # print(bigArr[i], arr[bigArr[i]])
                    if arr[bigArr[i]]> arr[maxIdx]:
                        maxIdx=bigArr[i]
                        # print( maxIdx, arr[maxIdx])
                    lastIdx=i
                
                    # minVal
            
            lastIdx= max(lastIdx, minIdx)
            # print(maxIdx,"-",arr[maxIdx] , "min",minIdx, arr[minIdx], lastIdx)
            l=lastIdx+1
            minIdx=lastIdx+1
            
            chunk+=1

        return chunk
        