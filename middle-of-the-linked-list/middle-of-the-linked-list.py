# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and not head.next:
            return head
        count = 0
        midNode = head
        current = head
        while current != None:
            if count % 2:
                midNode = midNode.next
            current = current.next
            count += 1
        return midNode
        
        