# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), final:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        final_res = []
        if not root:
            return []

        while queue:
            length = len(queue)
            temp = []

            for i in range(length):
                res = queue.pop(0)
                temp.append(res.val)
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
            
            final_res.append(temp)

        return final_res
        