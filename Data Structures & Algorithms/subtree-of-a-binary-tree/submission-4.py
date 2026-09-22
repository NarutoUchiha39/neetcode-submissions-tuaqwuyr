# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def SameTree(node1,node2):
           
            if (not node1) and (not node2):
                    return True

            elif ((not node1 and node2) or(not node2 and node1)) or (node1.val!=node2.val):
                return False

            res1 = SameTree(node1.left,node2.left)
            if not res1:
                return False
            res2 = SameTree(node1.right, node2.right)
            if not res2:
                return False

            return True

        def SubTree(node1,node2):
            if (not node1):
                return False

            val1 = SubTree(node1.left,node2)
            if val1:
                return True
            val2 = SubTree(node1.right,node2)
            if val2:
                return True     

            if (node1.val == node2.val):
                res = SameTree(node1,node2)
                if res:
                    return True
                else:
                    return False
            
            return False

        return SubTree(root,subRoot)