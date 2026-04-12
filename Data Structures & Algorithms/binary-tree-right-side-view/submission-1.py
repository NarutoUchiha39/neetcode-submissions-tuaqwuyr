class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        value = []

        if(not root):
            return []
         
        while(stack):
            root1 = None
            for i in range(len(stack)):
                element = stack.pop(0)
                root1 = element
                if(element.left != None):
                    stack += [element.left]
                if(element.right != None):
                    stack += [element.right]

            value.append(root1.val)

        return value

            
            
        
        
        

            
            
                



                
                

            