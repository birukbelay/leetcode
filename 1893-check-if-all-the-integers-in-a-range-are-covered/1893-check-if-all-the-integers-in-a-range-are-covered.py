class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        ctr = ranges[0][0]
        q=set()
        for i in range(left, right +1):
            q.add(i)
            
        # print(ranges)
        if ranges[0][0]>left:
            return False
        for i in ranges:
            # print(ctr, i)
            for j in range(i[0], i[1]+1):
                if j in q:
                    q.discard(j)
            
        # print(q)
        if q:
            return False
        else:
            return True
            
                
            