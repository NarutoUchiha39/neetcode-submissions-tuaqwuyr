# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def search_proxy(node):
            while(node.left):
                prev = node
                node = node.left
            return node
            
        def Search(node,key,prev):
            if not node:
                return None

            # print(node.val)
            if key>node.val:
                node.right = Search(node.right,key,node)
            
            elif key<node.val:
                node.left = Search(node.left,key,node)
            
            else:
                # print(node.left,node.right)
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                
                node.val = search_proxy(node.right).val
                node.right = Search(node.right,node.val,node)
            
            return node


        return Search(root,key,None)
        # return root







                