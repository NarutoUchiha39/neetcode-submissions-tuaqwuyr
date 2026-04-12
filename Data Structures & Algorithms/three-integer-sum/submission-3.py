from copy import deepcopy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        list1 = []
        set1 = set()
        
        if nums[0] == nums[-1]:
            if nums[0] == 0:
                return [[0, 0, 0]]
            else:
                return []
            
        for i in range( len(nums) ):
            mid = i + 1
            right = len(nums) - 1
            if(nums[i] == nums[i-1]):
                continue
            while( mid < right ):
                sum1 = nums[mid] + nums[right] + nums[i]
                if(sum1 == 0):
                    tuple1 = tuple([ nums[i],nums[mid],nums[right] ])
                    set1.add(tuple1)
                    mid += 1
                    right -= 1
                    
                elif(sum1 > 0):
                    right-=1
                else:
                    mid+=1
        list1 = [list(tup) for tup in set1]
        
        return list1