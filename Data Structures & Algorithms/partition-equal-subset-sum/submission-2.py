class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        tot = sum(nums)
        visited = [False for _ in range(len(nums))]
        def DFS(x,index):
            # print(x,index)
            if x>(tot - x):
                return False
            if x == (tot - x):
                return True
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if DFS(x+nums[i],i):
                        return True
                    visited[i] = False
            return False
        
        return DFS(0,-1)

