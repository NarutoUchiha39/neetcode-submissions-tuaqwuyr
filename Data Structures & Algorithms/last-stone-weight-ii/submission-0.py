class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum //2
        dp = {}
        
        def DFS(i,total):

            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))

            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] =  min(DFS(i+1,total),DFS(i+1,total+stones[i]))
            return dp[(i,total)]
        return DFS(0,0)