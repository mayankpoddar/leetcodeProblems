# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getToLeaf(self, root, prefix):
        results = []
        if (not root.left) and (not root.right):
            results.append(prefix + str(root.val))
            return results
        if root.left:
            results.extend(self.getToLeaf(root.left, prefix+str(root.val)))
        if root.right:
            results.extend(self.getToLeaf(root.right, prefix+str(root.val)))
        return results
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        for possible in self.getToLeaf(root, ""):
            n = len(possible)
            for i in range(n):
                res += int(possible[i])*(2**(n-i-1))
        return res