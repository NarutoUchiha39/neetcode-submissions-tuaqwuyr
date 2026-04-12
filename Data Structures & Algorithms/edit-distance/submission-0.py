class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        DP = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word2)):
            DP[len(word1)][i] = len(word2)-i
        for j in range(len(word1)):
            DP[j][len(word2)] = len(word1) - j
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    DP[i][j] = DP[i+1][j+1]
                else:
                    DP[i][j] = 1+min(DP[i+1][j],DP[i][j+1],DP[i+1][j+1])
        
        return(DP[0][0])

            
