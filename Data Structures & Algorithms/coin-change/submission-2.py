class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        # for i in coins:
        #     dp[i] = 1
        if amount == 0:
            return 0
        
        for index,element in enumerate(dp):
            for j in coins:
                if index>=j:
                    rem = index - j
                    if rem == 0:
                        dp[index] = 1
                    else:
                        # print(rem,element,j,index)
                        dp[index] =  min(1 + dp[rem],dp[index])
        
        # print(dp)
        return -1 if dp[-1] == float("inf") else dp[-1]
