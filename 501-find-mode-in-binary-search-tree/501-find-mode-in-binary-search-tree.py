# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def updateFreqDict(self, root, freqDict):
        count = freqDict.get(root.val, 0)
        count += 1
        freqDict[root.val] = count
        if root.left:
            self.updateFreqDict(root.left, freqDict)
        if root.right:
            self.updateFreqDict(root.right, freqDict)
        
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        freqDict = {}
        self.updateFreqDict(root, freqDict)
        current_modes = []
        current_max_count = 0
        for val, count in freqDict.items():
            if count > current_max_count:
                current_max_count = count
                current_modes = [val]
            elif count == current_max_count:
                current_modes.append(val)
        return current_modes
        
        