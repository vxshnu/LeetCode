# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #my initial approach

        # if head:
        #     dupli = [head.val]
        # curr = head
        # while curr and curr.next:
        #     if curr.next.val not in dupli:
        #         dupli.append(curr.next.val)
        #     else:
        #         curr.next = curr.next.next
        #         continue
        #     curr = curr.next
        # return head

        #efficient approach

        if not head:
            return None
        curr = head
        while curr:
            while curr.next and curr.next.val  == curr.val:
                curr.next = curr.next.next
            curr = curr.next

        return head
