# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def DFS( head, min1, max1):
            if(not head):
                return True
            
            elif(not(min1 < head.val and max1 > head.val)):
                return False
            
                
            return DFS(head.left, min1, head.val) and DFS(head.right, head.val, max1)
        
        return DFS(root,float("-inf"),float("inf"))