# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def SameTree(node1,node2):
            if (not node1) or (not node2):
                if ((not node1) and node2) or ((not node2) and node1):
                    return False
                return True

            elif (node1.val!=node2.val):
                return False
            
            res1 = SameTree(node1.left,node2.left)
            if not res1:
                return False
            res2 = SameTree(node1.right, node2.right)
            if not res2:
                return False

            return True
        
        return SameTree(p,q)

