# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(p,q):
            if(not p and not q):
                return True

            elif((not p and q) or (not q and p) ):
                return False
            
            left = DFS(p.left,q.left) 
            right = DFS(p.right,q.right)

            if(left and right):
                if(p.val == q.val):
                    return True
                else:
                    return False
            else:
                return False

        return DFS(p,q)
            

        