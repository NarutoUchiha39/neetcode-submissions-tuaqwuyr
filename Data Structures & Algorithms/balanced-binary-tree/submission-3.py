# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def reccur(node):
            if not node:
                return -1
            
            left = reccur(node.left)
            if(left == -2):
                return -2
            right = reccur(node.right)
            if(right == -2):
                return -2

            # print(left,right,node.val)

            if abs(left-right)>1:
                return -2
            
            return max(1+left,1+right)
        
        return True if reccur(root) != -2 else False
