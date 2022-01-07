# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head and not head.next:
            return head
        newHead = head.next
        temp = self.swapPairs(newHead.next)
        newHead.next = head
        head.next = temp
        return newHead
        