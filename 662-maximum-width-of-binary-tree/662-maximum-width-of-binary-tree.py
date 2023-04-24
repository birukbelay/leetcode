# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d={}
        self.maxN= 0
        self.maxTup=(sys.maxsize, -sys.maxsize)
    def widthOfBinaryTree(self, root: Optional[TreeNode], level=0) -> int:
        
        
        self.width(root, 0,0)
        
        # print(self.d)
        return self.maxN   
    
    
    
    def width(self, root: Optional[TreeNode], level, index):
        if not root:
            return
        
        tup= self.d.get( level, (float('inf'), float('-inf')))
        
        self.d[level]=(min(tup[0], index), max(tup[1], index))
        # self.maxTup=(min())
        self.maxN= max(self.maxN, self.d[level][1]-self.d[level][0] +1)
        
        self.width(root.left, level+1, index*2)
        self.width(root.right, level+1, (index*2)+1)
        
        
        
        
        