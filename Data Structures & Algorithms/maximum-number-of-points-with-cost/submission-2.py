from functools import cache
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        columns = len(points[0])
        dp = points[0]
        for i in range(1,rows):
            left = [0 for _ in range(columns)]
            right = [0 for _ in range(columns)]
            left[0] = dp[0]
            right[-1] = dp[columns-1]

            for j in range(1,columns):
                left[j] = max(dp[j],left[j-1]-1)

            for j in range(columns-2,-1,-1):
                right[j] = max(dp[j],right[j+1]-1)
            
            temp = points[i][:]
            for j in range(columns):
                temp[j]+=max(left[j],right[j])
            dp = temp

        return max(dp)
