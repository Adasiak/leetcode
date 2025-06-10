# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        tail = result

        while lists:
            idx_of_min = min((i for i, node in enumerate(lists) if node),key=lambda i: lists[i].val, default=None)
            if idx_of_min == None:
                lists.remove(idx_of_min)
                continue
            tail.next = lists[idx_of_min]
            # lists[idx_of_min] = lists[idx_of_min].next
            tail = tail.next

            if lists[idx_of_min].next:
                lists[idx_of_min] = lists[idx_of_min].next
            else:
                lists.pop(idx_of_min)

            print(tail.val)


        return result.next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Remove None lists
    lists = [lst for lst in lists if lst is not None]

    # Create a dummy head for the result
    dummy = ListNode()
    tail = dummy

    while lists:
        # Find the minimum node
        min_index = 0
        for i in range(1, len(lists)):
            if lists[i].val < lists[min_index].val:
                min_index = i

        # Add the minimum node to the result
        tail.next = lists[min_index]
        tail = tail.next

        # Update the list
        if lists[min_index].next:
            lists[min_index] = lists[min_index].next
        else:
            lists.pop(min_index)

    return dummy.next


lists1 = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]

oo = mergeKLists(lists=lists1)
expected = [1, 1, 2, 3, 4, 4, 5, 6]

if oo != expected:
    print(oo, "not equal", expected)
    raise ValueError
# print("kapusta", mergeKLists(lists=lists1))