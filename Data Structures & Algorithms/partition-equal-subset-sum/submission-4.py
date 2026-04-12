class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        target = sum(nums) // 2
        dp = [[False]*(target+1) for i in nums]

        for i in range(len(nums)):
            for j in range(target+1):
                # print(nums[i],j)
                if nums[i] == j:
                    dp[i][j] = True
                # elif nums[i] > j:
                #     continue
                elif(i>0):
                    if j>=nums[i]:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                    else:
                        dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[-1][-1]