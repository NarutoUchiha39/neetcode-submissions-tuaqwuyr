class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        divide = sum(nums) // k
        remainder = sum(nums) % k
        if remainder != 0:
            return False

        visited = [False for _ in range(len(nums))]
        def DFS(k,index,curSum):
            if k == 0:
                return True
            elif curSum == divide:
                return DFS(k-1,0,0)

            for i in range(index,len(nums)):
                if visited[i] or (curSum + nums[i] > divide):
                    continue
                visited[i] = True
                res = DFS(k,i,curSum+nums[i])
                if res:
                    return True
                visited[i] = False

            return False
        return DFS(k,0,0)

            