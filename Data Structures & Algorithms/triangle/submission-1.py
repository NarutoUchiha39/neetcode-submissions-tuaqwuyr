from functools import cache

class Solution:
    def minimumTotal(self, triangles: List[List[int]]) -> int:
        
        @cache
        def DFS(point):
            x = point[0]
            y = point[1]
            if x>=len(triangles) or y >= len(triangles[x]):
                return 0
            
            return triangles[x][y]+min(DFS((x+1,y)),DFS((x+1,y+1)))   

        return DFS((0,0))