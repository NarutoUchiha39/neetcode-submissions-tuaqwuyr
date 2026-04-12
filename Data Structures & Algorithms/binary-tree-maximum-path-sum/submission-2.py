class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global max_sum
        global cur_sum
        max_sum = float("-inf")
        cur_sum  = 0

        def DFS(root):
            global max_sum
            if(not root):
                return 0

            left = DFS(root.left)
            right = DFS(root.right)
            
            left  = max(0,left)
            right  = max(0,right)

            max_sum = max(max_sum,left + right + root.val) 
            return root.val + max(left,right)
        DFS(root)
        return max_sum


            
        