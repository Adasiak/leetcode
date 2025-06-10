from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head node to simplify handling the merged list
        dummy = ListNode()         # wartownik
        tail  = dummy              # wskaźnik na koniec wyniku

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1  # dokładamy węzeł z list1
                list1 = list1.next
            else:
                tail.next = list2  # dokładamy węzeł z list2
                list2 = list2.next
            tail = tail.next       # przesuwamy ogon

        # jedna z list mogła się skończyć — doczep resztę drugiej
        tail.next = list1 or list2

        return dummy.next











def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    tail = result
    
    while list1 and list2:
        if list1 <= list2:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
            
        tail = tail.next 
    
    tail.next = list1 or list2
    
    return result.next










def mergeTwoLists_v3(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    tail = result
    
    while list1 and list2:
        if list1 <= list2:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list1
            list1 = list1.next
        
        tail = tail.next    
            
    tail.next = list1 or list2
    
    return tail.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

expected = [1, 1, 2, 3, 4, 4]

if merged_list != expected:
    print(merged_list, "not equal", expected)
    raise ValueError