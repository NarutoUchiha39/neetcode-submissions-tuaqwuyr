import math
class Solution:
    def numSquares(self, n: int) -> int:
        limit = math.floor(math.sqrt(n))
        nums = [i**2 for i in range(limit+1)]
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 0
        # print(dp)
        for i in range(len(dp)):
            for j in nums:
                if i < j:
                    continue
                else:
                    dp[i] = min(dp[i],1+dp[i-j])
        # print(nums)
        # print(dp)
        return dp[-1]
        

        