class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        arr = [0,0]
        arr2 = [0,0]

        for i in range(len(nums)-1):
            temp = arr[0]
            arr[0] = nums[i] + arr[1]
            arr[1] = max(temp,arr[1])
        
        
        for i in range(1,len(nums)):
            temp = arr2[0]
            arr2[0] = nums[i] + arr2[1]
            arr2[1] = max(temp,arr2[1])
        
        return max(max(arr),max(arr2))
        