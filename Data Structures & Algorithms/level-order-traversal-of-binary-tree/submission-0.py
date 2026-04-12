# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if(not root):
            return []
        stack = [root]
        value = [[root.val]]
        
        while(stack):
            
            list1 = []
            for i in range(len(stack)):
                element = stack.pop(0)
                if(element.left):
                    list1+=[element.left.val]
                    stack.append(element.left)
              
                    
                if(element.right):
                    list1+=[element.right.val]
                    stack.append(element.right)
                
            value.append(list1)
        value.pop()
        return value
                    
                    
            
            
        