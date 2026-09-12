# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def postorderTraversal(node):
            if not node:
                return
            
            postorderTraversal(node.left)
            if node.left:
                res.append(node.left.val)
            postorderTraversal(node.right)
            if node.right:
                res.append(node.right.val)
            
        
        postorderTraversal(root)
        if root:
            res.append(root.val)
        return res