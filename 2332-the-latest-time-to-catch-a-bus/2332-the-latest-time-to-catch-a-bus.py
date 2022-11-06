class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        d=collections.Counter(passengers)
        tCapacity=capacity * len(buses)
        
        pasLen=len(passengers)
        br, pr=len(buses)-1, pasLen-1
        
        print("p=",passengers)
        print("b=",buses)

        maxTime= max(0, passengers[0]-1)
        cur=0
        # to find the last index of user who climbs on the bus || all must be fulfiled
        for t in buses:
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= t and cap > 0:
                cur += 1
                cap -= 1
        print('t--',t)
        
        # if it still have capacity
        best = t if cap > 0 else passengers[cur -1]
        
        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best
        
            
            
            
            
            
                
                
                
        

        