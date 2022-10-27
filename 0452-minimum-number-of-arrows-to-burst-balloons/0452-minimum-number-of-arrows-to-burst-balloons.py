class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        ctr=1
        end=points[0][1]
        for i,v in enumerate(points):
            if end < v[0]:
                ctr+=1
                end=v[1]
            else:
                end=min(end, v[1])
        return ctr