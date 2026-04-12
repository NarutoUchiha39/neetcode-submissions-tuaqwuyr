class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        set1 = set()
        def DFS(sum1,index):
            if index == len(nums):
                # print(sum1,index)
                if sum1 == target:
                    return 1
                else:
                    return 0

            total_ways = 0
            # for i in range(len(nums)):
            # if i > index:
            add = DFS(sum1+nums[index],index+1)
            subtract = DFS(sum1-nums[index],index+1)
            total_ways = total_ways+add+subtract
                
            return total_ways

        return DFS(0,0)    

                    
