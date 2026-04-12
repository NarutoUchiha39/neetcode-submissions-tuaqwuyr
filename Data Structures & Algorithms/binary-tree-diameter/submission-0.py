# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        global maximum_dia
        maximum_dia = float("-inf")

        def DFS( root ):
            global maximum_dia 
            if not root:
                return -1
            
            left = 1 + DFS(root.left)
            right = 1 + DFS(root.right)
            
            path = left + right
            maximum_dia = max( maximum_dia, path )
            return  max(left,right)

        DFS(root)
        return maximum_dia

        