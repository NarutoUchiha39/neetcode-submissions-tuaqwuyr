class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            cur_sum = running_sum + nums[i]
            running_sum = max(cur_sum,nums[i])
            max_sum = max(max_sum,running_sum)

        return max_sum

        