# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]
        if not root:
            return []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                val = queue.pop(0)
                if val:
                    if (not val.left) or (not val.right):
                        temp.append(None)
                    if(val.left):
                        temp.append(val.left)
                        queue.append(val.left)
                    if(val.right):
                        temp.append(val.right)
                        queue.append(val.right)

        
            for i in temp[::-1]:
                if i:
                    res.append(i.val)
                    break
        
        return [root.val]+res


