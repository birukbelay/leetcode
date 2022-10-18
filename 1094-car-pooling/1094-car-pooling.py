class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dist=[0]*1000
        
        for i in trips:
            pas, fr,to = i[0],i[1],i[2]
            dist[fr]+=pas
            if to < len(dist)-1:
                dist[to]-=pas
        
        temp=0
        for i in range(len(dist)):
            dist[i]+=temp
            temp=dist[i]
            if dist[i]>capacity:
                return False
        return True