# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def level_order_traversal( root ):
            
            if(not root):
                return ""
            array = [ root ]
            string =  ""
            while(array):
                string_sublevel = ""
                for i in range(len(array)):
                    element = array.pop(0)
                    if(element == None):
                        string_sublevel = string_sublevel + "$,"
                    else:
                        string_sublevel = string_sublevel + str(element.val) +","
                    
                    if(element):
                        array.append(element.left)
                        array.append(element.right) 
                        
                string_sublevel = string_sublevel[0:len(string_sublevel)-1] + ";"
                string = string + string_sublevel
            
            return string
        return level_order_traversal(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        
        array = data.split(";")
        array.pop()
        head = TreeNode(array[0])
        stack = [ head ]
        
        
        while(stack):
            array.pop(0)
            low = 0
            high = 2

            for i in range(len(stack)):
                element = stack.pop(0)
                temp = array[0].split(",")
                
                
                for k in range(low,high-1):
                    
                    if(temp[k] == "$"):
                        element.left = None
                    if(temp[k+1] == "$" ):
                        element.right = None
                    if(temp[k] != "$"):
                        
                        left = TreeNode(temp[k])
                        element.left = left
                        stack.append(left)
                        
                    if(temp[k+1] != "$"):
                        
                        right = TreeNode(temp[k+1])
                        element.right = right
                        stack.append(right)
                        
                        
                low += 2
                high += 2
                
        return head
                    
            
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
