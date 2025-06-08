from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0,
                 left: Optional['TreeNode']=None,
                 right: Optional['TreeNode']=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res   = []
        queue = deque([root])               # ① startujemy od korzenia

        while queue:                        # ② dopóki coś jest w kolejce
            level_size = len(queue)         # ③ liczba węzłów na tym poziomie
            level_vals = []

            for _ in range(level_size):     # ④ dokładnie tyle iteracji
                node = queue.popleft()      #    (FIFO ⇒ BFS)
                level_vals.append(node.val)

                if node.left:               # ⑤ wrzucamy dzieci
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_vals)          # ⑥ poziom gotowy

        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        que = deque([root])
        
        while que:
            level_size = len(que)
            level_vals = []
            
            for _ in range(level_size):
                node = que.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    level_vals.append(node.left)
                if node.right:
                    level_vals.append(node.right)
            res.append(level_vals)
        
        return res
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        response = []
        que = deque([root])
        while que:
            level_size = len(que)
            level_val = []
            for _ in range(level_size):
                node = que.popleft()
                level_val.append(node.val)
                if node.left:
                    level_val.append(node.left)
                if node.right:
                    level_val.append(node.right)
            response.append(level_val)
        return response
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        list_to_return = []
        q = deque([root])
        while q:
            level_size = len(q)
            level_val = []
            
            for _ in range(level_size):
                node = q.popleft()
                level_val.append(node.val)
                if node.left:
                    level_val.append(node.left)
                if node.right:
                    level_val.append(node.right)
            list_to_return.append(level_val)
        return list_to_return
    
    
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        list_to_return = []
        q = deque([root])
        while q:
            level_size = len(q)
            level_val = []
            for _ in range(level_size):
                node = q.popleft()
                level_val.append(node.val)
                if node.left:
                    level_val.append(node.left)
                if node.right:
                    level_val.append(node.right)
            list_to_return.append(level_val)
        return list_to_return