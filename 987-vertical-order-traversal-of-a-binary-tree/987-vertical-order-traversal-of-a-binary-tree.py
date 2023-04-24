# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d={}
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.visit(root, 0,0)
        # print(self.d)
        
        a=dict(sorted(self.d.items()))
        arr=[]
        for k,v in a.items():
            # print(v)
            m=sorted(v)
            
            arr.append([a[1] for a in m])
        return arr
            
    
    
    def visit(self,root, row, col):
        if not root:
            return
        di= self.d.get(col, [])
        di.append((row, root.val))
        self.d[col]=di
        
        if root.left:
            self.visit(root.left, row+1, col-1)
        if root.right:
            self.visit(root.right, row+1, col+1)
        
        
        
        