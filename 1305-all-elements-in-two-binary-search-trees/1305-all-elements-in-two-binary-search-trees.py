# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getInorder(self, root, result):
        if root:
            self.getInorder(root.left, result)
            result.append(root.val)
            self.getInorder(root.right, result)
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        inorder1 = []
        inorder2 = []
        self.getInorder(root1, inorder1)
        self.getInorder(root2, inorder2)
        result = []
        i = 0
        j = 0
        n1 = len(inorder1)
        n2 = len(inorder2)
        while i < n1 or j < n2:
            if i < n1 and j < n2:
                if inorder1[i] <= inorder2[j]:
                    result.append(inorder1[i])
                    i += 1
                else:
                    result.append(inorder2[j])
                    j += 1
            else:
                if i < n1:
                    result.append(inorder1[i])
                    i += 1
                else:
                    result.append(inorder2[j])
                    j += 1
        return result