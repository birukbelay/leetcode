# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        d= {}
        res=0
        def dfs(l, d, node):
            nonlocal res
            if not node:
                return 
            
            d[l]=node.val%2==0
            if l>2 and d[l-2]:
                res+=node.val
            dfs(l+1, d, node.right)
            dfs(l+1, d, node.left)
        dfs(1, d, root)
        return res