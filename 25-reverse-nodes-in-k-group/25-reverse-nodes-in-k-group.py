# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        current = head
        count = 1
        arr = []
        while current and count != k:
            arr.append(current.val)
            current = current.next
            count += 1
        if not current:
            return head
        arr.append(current.val)
        current = head
        for i in range(k):
            current.val = arr[k-1-i]
            current = current.next
        self.reverseKGroup(current, k)
        return head