
# import time

# current_time = time.ctime()
# print(current_time)
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # sort by reversed growing time & plant
        nSet=[]
        maxGrow=0
        curPlant=0
        for i in range(len(growTime)):
            nSet.append((growTime[i], i))
        
        nSet.sort(reverse=True)
        
        for g, i in nSet:
            curPlant+= plantTime[i]
            curGrow=curPlant+g
            maxGrow= max(maxGrow, curGrow)
        return maxGrow
            
        
        