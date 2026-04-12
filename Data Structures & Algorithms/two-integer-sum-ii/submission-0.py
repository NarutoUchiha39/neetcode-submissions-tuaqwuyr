class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            right = i+1
            while(right < len(nums)):
                if(nums[i] + nums[right] == target):
                    return[i+1,right+1] 
                right+=1

        