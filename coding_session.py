# Given the head of a singly linked list, swap every two adjacent nodes and return the head of the modified list.
# You cannot modify the values inside the nodes. You must actually change the node connections.

# Input:
# 1 → 2 → 3 → 4 

# Output:
# 2 → 1 → 4 → 3

# Input:
# 1 → 2 → 3

# Output:
# 2 → 1 → 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # Swap
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to the next pair
        prev = first

    return dummy.next

