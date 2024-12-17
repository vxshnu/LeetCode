# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique = list()
        node = head
        while node is not None:
            if node in unique:
                return True
            unique.append(node)
            node = node.next
        return False