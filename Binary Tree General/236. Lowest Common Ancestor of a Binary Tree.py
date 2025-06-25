# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: TreeNode):
            if not root:
                return
            elif root is p or root is q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                return root
            
            return left if left else right
        return dfs(root)
    
 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: TreeNode):
            if not root:
                return
            elif root is p or root is q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            return left if left else right
        return dfs(root)
    

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: TreeNode):
            if not root:
                return
            if root is p or root is q:
                return root
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l and r:
                return root
            
            return l if l else r