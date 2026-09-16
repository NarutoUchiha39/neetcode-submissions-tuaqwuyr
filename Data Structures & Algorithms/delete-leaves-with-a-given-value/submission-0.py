# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def reccur(node):
            if not node:
                return True

            left = reccur(node.left)
            right = reccur(node.right)

            if left == True:
                node.left = None
            if right == True:
                node.right = None

            if (left and right and node.val == target):
                return True

            return False
        
        res = reccur(root)
        return None if res else root

        