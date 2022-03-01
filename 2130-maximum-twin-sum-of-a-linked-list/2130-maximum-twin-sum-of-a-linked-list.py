# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxTwinSum = 0
        current = head
        elements = []
        while current != None:
            elements.append(current.val)
            current = current.next
        n = len(elements)
        for i in range(n//2):
            maxTwinSum = max(maxTwinSum, elements[i] + elements[n-i-1])
        return maxTwinSum
            
        