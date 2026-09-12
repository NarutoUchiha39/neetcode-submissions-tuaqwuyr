# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         
        res = []
        def InOrder(node):
            if not node:
                return

            InOrder(node.left)
            if node:
                res.append(node.val)
            
            InOrder(node.right)

            
        InOrder(root)
        return res

