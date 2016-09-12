"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
"""
Merge two sorted lists. l1 and l2 are Node objects.

Runtime Complexity: O(N)
Space Complexity: O(1) -- only created 1 extra dummy node (head node)
"""
def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    head = temp = Node(0)
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next

    if l1 is not None or l2 is not None:
        longer = l2 if l1 is None else l1
        while longer is not None:
            temp.next = longer
            temp = temp.next
            longer = longer.next

    return head.next
