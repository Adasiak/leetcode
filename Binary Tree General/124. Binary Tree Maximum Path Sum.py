# Definition for a binary tree node.
from typing import Optional

# BEST = float("-inf")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # BEST = float("-inf")
        
        def dfs(node: Optional[TreeNode]):
            global BEST
            if node:
                left = max(0, dfs(node.left))
                right = max(0, dfs(node.right))
                
                BEST = max(BEST, node.val + left + right)
                return node.val + max(left, right)
            return 0
        dfs(root)
        return BEST
    
    
# BEST = float("-inf")      # globalny rekord (–∞ na start)

# def dfs(node):
#     global BEST
#     if node is None:      # pusty podwęzeł nie wnosi zysku
#         return 0

#     # 1) maksymalny „zysk” z lewej i prawej gałęzi,
#     #    ale ujemny przycinamy do zera (wtedy gałąź ignorujemy)
#     left  = max(0, dfs(node.left))
#     right = max(0, dfs(node.right))

#     # 2) ścieżka przechodząca PRZEZ bieżący węzeł:
#     #    lewa gałąź + węzeł + prawa gałąź
#     BEST = max(BEST, node.val + left + right)

#     # 3) wartość zwracana w górę – to JEDNA gałąź
#     #    (węzeł + lepsza z dwóch stron)
#     return node.val + max(left, right)



class Solution:
    best = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # best = float("-inf")
        def dfs(node: Optional[TreeNode]):
            if not node:
                return node
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.best
        



class Solution:
    best = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.best
    

    
class Solution:
    best = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.best