"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    def connectHelper(self, root, levels, currentLevel):
        if root:
            self.connectHelper(root.right, levels, currentLevel+1)
            next_right = levels.get(currentLevel, None)
            root.next = next_right
            levels[currentLevel] = root
            self.connectHelper(root.left, levels, currentLevel+1)
    
    def connect(self, root: 'Node') -> 'Node':
        levels = {}
        self.connectHelper(root, levels, 0)
        return root
        