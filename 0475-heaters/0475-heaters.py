class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters=list(set(heaters))
        houses=list(set(houses))
        houses.sort()
        heaters.sort()
        
        N = len(houses)
        jmax=len(heaters)-1
        # maxEnd = max(abs(heaters[0]-houses[0]), abs(heaters[-1]-houses[-1]))
        maxDis=-sys.maxsize
        # heaters index
        j=0
        for _,v in enumerate(houses):
            # find the closest heater to V
            # print(i,v)
            
            hdis= abs(v-heaters[j])
            
            while j < jmax and abs(v-heaters[j]) > abs(v-heaters[j+1]):
                j+=1
                hdis= min(hdis, abs(heaters[j]-v))
                        
            maxDis = max(maxDis, hdis)
        # halfDis = maxDis // 2 if maxDis %2 ==0 else (maxDis // 2) +1
        return maxDis