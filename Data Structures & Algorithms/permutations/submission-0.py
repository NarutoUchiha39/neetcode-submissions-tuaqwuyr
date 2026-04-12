from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        temp = []
        glob_set = set()

        def DFS():
            
            if(len(temp) == len(nums)):
                res.append( deepcopy(temp) )
                return
            
            for i in range(len(nums)):
                if i not in glob_set:

                    temp.append(nums[i])
                    glob_set.add(i)
                    DFS()
                    glob_set.remove(i)
                    temp.pop()
            

        DFS()
        return res
