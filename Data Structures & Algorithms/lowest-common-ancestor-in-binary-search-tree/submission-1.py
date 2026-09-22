# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def LCA(node):
            if(not node):
                return TreeNode(-1000)

            left1 = LCA(node.left)
            right1 = LCA(node.right)
            
            if (node.val == p.val):
                return p
            elif (node.val == q.val):
                return q
            
            elif(left1.val != -1000 and right1.val!=-1000):
                return node
            elif(left1.val!= -1000 and right1.val==-1000):
                return left1

            elif(left1.val== -1000 and right1.val!=-1000):
                return right1
            
            
            return TreeNode(-1000)

        return LCA(root)
