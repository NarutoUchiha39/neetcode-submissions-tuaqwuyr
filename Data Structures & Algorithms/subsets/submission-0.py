from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        global subset
        subset = []

        def DFS( nums,list1,num ):
            global subset
            
            if(len(list1) == num):
                subset.append(deepcopy(list1))
                return 
                
            if(not nums):
                return

            for i in range(len(nums)):
                list1.append(nums[i])
                DFS(nums[i+1:],list1,num)
                list1.pop()
        
        for i in range(len(nums)+1):
            DFS(nums,[],i)
        return subset
                

            
            
            