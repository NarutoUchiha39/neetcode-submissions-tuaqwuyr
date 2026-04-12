class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1 if i in nums else 0 for i in range(target+1)]
        if target == 0:
            return 1
        for i in range(target+1):
            for j in nums:
                if i < j:
                    continue
                else:
                    dp[i] += dp[i-j]
        
        return dp[-1]
        