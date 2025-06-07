# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print(root)
        # tmp = root
        def check(root1: TreeNode, root_val:int, right:bool):
            left = root1.left
            right = root1.right
            if left and left.val >= root1.val and right == False and left.val >= root_val:
                return False, False
            if right and root1.val >= right.val and right == True and right.val <= root_val:    
                return False, False
            # else:
            #     return None, None
            return left, right
        tmp_list = []
        tmp = root
        root_val = tmp.val
        right = None
        while True:
            left, right = check(tmp)
            if left == False or right == False:
                return False
            if left:
                tmp = left
                if right:
                    tmp_list.append((right, root_val))
            elif right:
                tmp = right
                root
            elif tmp_list:
                tmp = tmp_list.pop()
            else:
                return True
                
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):        # złamanie reguły BST
                return False
            return (dfs(node.left,  low,  node.val) and
                    dfs(node.right, node.val, high))

        # -inf i +inf na start
        return dfs(root, float("-inf"), float("inf"))
                
            
            
            


def isValidBts( root: Optional[TreeNode]) -> bool:
    def check(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        
        return (check(node.left, low, node.val) and check(node.right, node.val, high))
    
    return check(root, float("-inf"), float("inf"))
    
    
def isValid(root : Optional[TreeNode]):
    def check(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (
                check(node.left, low, node.val)
                and
                check(node.right, node.val, high)
            )        
        
    return check(root, float("-inf"), float("inf"))