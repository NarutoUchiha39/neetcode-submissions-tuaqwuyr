# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global inorder 
        inorder = []
        
        def DFS(root):
            global inorder
            
            if not root:
                return None
            
            left = DFS(root.left)
            inorder += [root.val]
            right = DFS(root.right)
        
        DFS(root)
        print(inorder)
        return inorder[k-1]
            
            
            
            
