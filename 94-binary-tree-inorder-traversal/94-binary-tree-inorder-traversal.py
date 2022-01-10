# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inOrderTraversalHelper(self, root):
        results = []
        if root != None:
            results.extend(self.inOrderTraversalHelper(root.left))
            results.append(root.val)
            results.extend(self.inOrderTraversalHelper(root.right))
        return results
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inOrderTraversalHelper(root)
        