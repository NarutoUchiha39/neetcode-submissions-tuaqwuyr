# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        global balanced
        balanced = True

        def DFS( root ):
            global balanced

            if(balanced):
                if(not root):
                    return -1
                left  = 1 + DFS(root.left)
                right = 1 + DFS(root.right)

                if(abs(left - right) > 1 ):
                    balanced = False
                
                return max(left,right)
            else:
                return -1
        DFS( root )
        return balanced

            
        