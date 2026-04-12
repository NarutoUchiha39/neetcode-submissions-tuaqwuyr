class Solution:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(word))]

        for i in range(len(word)-1,-1,-1):
            for j in wordDict:
                if len(j) > len(word[i:]):
                    continue
                # elif dp[i] != True:
                dp[i] = j == word[i:i+len(j)]
                forward = i+len(j)
                # print(forward,j,word[i:],dp[i])
                if forward < len(word):
                    dp[i] = dp[i] and dp[forward]
                    # print(dp[i],dp[forward],i,forward)
                # print(dp)
                if dp[i] == True:
                    break

        
        # print(dp)
        return dp[0]
