class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[]
        tot=0
        N=len(heights)
        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1] >h:
                
                index, height = stack.pop()
                area= height * (i- index)
                tot =max(tot, area)
                start=index
            stack.append((start, h))
        
        for i,h in stack:
            tot= max(tot, h* (N-i))
        return tot