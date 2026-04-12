class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = [0]
        def construct(preorder,inorder):
            if(index[0] >= len(preorder) or not inorder):
                return None

            node = TreeNode()
            node.val = preorder[index[0]]

            element = preorder[index[0]]

            left = inorder[:inorder.index(element)]
            right = inorder[inorder.index(element)+1:]

            index[0] += 1

            node.left = construct(preorder,left)
            node.right = construct(preorder,right)

            return node
        return construct(preorder,inorder)


            


        