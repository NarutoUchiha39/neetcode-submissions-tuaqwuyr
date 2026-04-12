# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        global count 
        count = 0
        
        def DFS(head,largest):
            global count 
            if(not head):
                return 
            
            elif(head.val >= largest):
                count += 1
            
            DFS(head.left,max(head.val,largest))
            DFS(head.right,max(head.val,largest))
        
        DFS(root,root.val)
        
        return count        
            
            
        