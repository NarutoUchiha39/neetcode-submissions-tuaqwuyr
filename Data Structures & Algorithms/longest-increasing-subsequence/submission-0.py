class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        max_len =  float("-inf")
        for i in range(len(nums)-1,-1,-1):
            length = dp[i]
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    length = max(dp[i] + dp[j],length)
            dp[i] = length
            max_len = max(max_len,length)

        # print(dp)
        return max_len