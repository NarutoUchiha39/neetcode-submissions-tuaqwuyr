class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        
        res = []
        left = []
        right_array = []
        cur_left = 1
        cur_right = 1

        for i in range(len(nums)):
            right = len(nums)-1-i
            if(i==0):
                left.append(1)
                
            if(right==len(nums)-1):
                right_array.append(1)
                
            else:
                left.append(left[-1]*nums[i-1])
                right_array.insert(0,right_array[0]*nums[right+1])
                
        return [left[i]*right_array[i] for i in range(len(nums))]           
            
           
            
            