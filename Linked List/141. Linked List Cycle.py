# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seq = []
        # for i in range(5):
        
        while head:
            # if head:
            print(head.val)
            seq.append(head.val)
            if len(seq) - len(set(seq)) > 5:
                return True
            head = head.next
        
        
        return False
    
    
class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:          # dopóki możemy wykonać 2 kroki
            slow = slow.next               # 1 krok
            fast = fast.next.next          # 2 kroki
            if slow is fast:               # spotkanie ⇒ cykl
                return True
        return False   
    


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False