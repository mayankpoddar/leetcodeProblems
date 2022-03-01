# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        currentSum = 0
        newHead = None
        existing = None
        while current != None:
            if current.val == 0:
                if currentSum != 0:
                    newNode = ListNode(currentSum)
                    if newHead == None:
                        newHead = newNode
                    else:
                        if existing == None:
                            newHead.next = newNode
                            existing = newNode
                        else:
                            existing.next = newNode
                            existing = existing.next
                    currentSum = 0
            else:
                currentSum += current.val
            current = current.next
        return newHead
        