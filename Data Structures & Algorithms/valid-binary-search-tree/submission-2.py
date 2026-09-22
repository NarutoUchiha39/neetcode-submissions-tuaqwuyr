# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        set1 = set()
        def InOrder(node):
            if not node:
                return None
            InOrder(node.left)
            res.append(node.val)
            InOrder(node.right)
        
        InOrder(root)
        res1 = res.copy()
        res1.sort()
        for i in res1:
            if i not in set1:
                set1.add(i)
            else:
                return False

        return res == res1
        