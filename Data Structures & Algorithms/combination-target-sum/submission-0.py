from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        total = []
        res = []
        
        def DFS(nums,cur_sum,target,i):
           
            if(cur_sum == target):
                res.append(deepcopy(total))
                return
            if(cur_sum > target or i >= len(nums)):
                return
            
            cur_sum += nums[i]
            total.append(nums[i])
            DFS(nums,cur_sum,target,i)
            
            cur_sum -= nums[i]
            total.pop()
            DFS(nums,cur_sum,target,i+1)
            
        DFS(candidates
            ,0,target,0)
        return res
                
            
            