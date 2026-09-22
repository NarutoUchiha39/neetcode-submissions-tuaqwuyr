# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        
        def Count(node,num):
            if not node:
                return

            if node.val>=num:
                count[0]+=1
            
            Count(node.left,num if node.val < num else node.val)
            Count(node.right,num if node.val < num else node.val)

        Count(root,float("-inf"))
        return count[0]