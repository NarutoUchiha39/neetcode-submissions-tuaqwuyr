# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS( head ):
            if(not head):
                return None
            
            left = DFS(head.left)
            right = DFS(head.right)
            
            head.right = left 
            head.left = right
            
            return head
        
        return DFS( root )
            
        