class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        ctr=0
        l,r=0, len(people)-1
        sw=0
        while l<=r:           
            
            if people[l] + people[r]<=limit:
                ctr+=1
                l+=1
                r-=1
            else:
                ctr+=1
                r-=1        
        return ctr
                
            
        