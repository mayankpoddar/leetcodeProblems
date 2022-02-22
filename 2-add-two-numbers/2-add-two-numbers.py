# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prevNode = None
        while l1 or l2:
            digit = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if digit > 9:
                carry = 1
                digit = digit - 10
            else:
                carry = 0
            newNode = ListNode(digit)
            if prevNode:
                prevNode.next = newNode
            else:
                head = newNode
            prevNode = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            newNode.next = ListNode(carry)
        return head