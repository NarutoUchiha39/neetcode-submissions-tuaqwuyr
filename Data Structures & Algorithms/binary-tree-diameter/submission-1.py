# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_element = [float("-inf")]
        def reccur(node):
            if not node:
                return -1

            left = 1+reccur(node.left)
            right = 1+reccur(node.right)   
            max_element[0] = max(max_element[0],left+right)
            return max(left,right)     

        res = reccur(root)
        return max(res,max_element[0])
