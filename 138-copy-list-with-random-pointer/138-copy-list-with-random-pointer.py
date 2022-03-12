"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        elements = {}
        current = head
        if not head:
            return None
        while current != None:
            elements[current] = Node(current.val)
            current = current.next
        for current, newNode in elements.items():
            if current.next:
                elements[current].next = elements[current.next]
            if current.random:
                elements[current].random = elements[current.random]
        return elements[head]        
        
        