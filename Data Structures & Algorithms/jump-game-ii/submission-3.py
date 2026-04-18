class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                dp[i] = float("inf")
                continue
            for j in range(1,nums[i]+1):
                if i+j >= len(nums):
                    dp[i] = min(dp[i],float("inf"))
                else:
                    if i+j == len(nums)-1:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i],1+dp[i+j])
        
        # print(dp)
        return dp[0] if dp[0]!=float("inf") else 0
            