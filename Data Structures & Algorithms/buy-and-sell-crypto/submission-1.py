class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        left = 0
        right = 0
        git_diff = float("-inf")

        while(right <= len(nums) -1):

            git_diff = max(git_diff,nums[right] - nums[left])

            if( nums[left] > nums[right] ):
                left = right
            right += 1
        
        return git_diff

        


            