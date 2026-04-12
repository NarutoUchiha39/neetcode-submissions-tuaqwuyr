from copy import deepcopy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        temp = []
        set1 = set()

        def DFS(index):
            
            if (index >= len(nums) ):
                
                temp2 = deepcopy(temp)
                temp2.sort()
                tup = tuple(temp2)
                
                if(tup not in set1):
                    res.append(temp2)
                    set1.add(tup)
                return

            temp.append(nums[index])
            DFS(index + 1)
            temp.pop()
            DFS(index + 1)
        
        DFS(0)
        return res

            


        