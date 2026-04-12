# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p,q):
            if(not p and not q):
                return True

            elif((not p and q) or (not q and p) ):
                return False
            
            left = sameTree(p.left,q.left) 
            right = sameTree(p.right,q.right)

            if(left and right):
                if(p.val == q.val):
                    return True
                else:
                    return False
            else:
                return False


        def DFS( p,q ): 
            if(not p):
                return False

            left = DFS( p.left,q ) 
            right = DFS( p.right,q )

            if(p.val == q.val):
                if(not(left or right)):
                    return sameTree(p,q)
                else:
                    return True

            return left or right

        return DFS(root,subRoot)
    
            

        
        
        