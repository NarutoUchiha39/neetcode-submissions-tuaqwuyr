# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def reccur(node):

            while not node:
                return [0,0]
            
            left_profit = reccur(node.left)
            right_profit = reccur(node.right)

            steal = node.val + left_profit[1] + right_profit[1]
            not_steal = max(left_profit)+ max(right_profit)

            return [steal,not_steal]
        return max(reccur(root))
