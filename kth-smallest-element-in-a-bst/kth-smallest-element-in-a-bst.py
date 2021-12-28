# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root):
        results = []
        if root:
            results.extend(self.inorder(root.left))
            results.append(root.val)
            results.extend(self.inorder(root.right))
        return results
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.inorder(root)
        return inorder[k-1]
        