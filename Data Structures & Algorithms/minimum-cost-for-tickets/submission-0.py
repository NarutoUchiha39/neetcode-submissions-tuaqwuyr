class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [ float("inf") if i in days else 0 for i in range(days[-1]+1)]
        
        dp[-1] = costs[0]
        for i in range(len(dp)-1,-1,-1):
            if dp[i] == 0:
                # print("Ok",i)
                dp[i] = dp[i+1] 
            else:
                for index,element in enumerate(costs):
                    if index == 0:
                        new = i+1
                    elif index == 1:
                        new = i+7
                    elif index == 2:
                        new = i+30
                    # print("=======>")
                    # print(new,dp[i])
                    # print("=======>")

                    if new >= len(dp):
                        dp[i] = min(dp[i],element)
                    else:
                        dp[i] = min(dp[i],element+dp[new])
        
        # print(dp)
        return dp[0]
