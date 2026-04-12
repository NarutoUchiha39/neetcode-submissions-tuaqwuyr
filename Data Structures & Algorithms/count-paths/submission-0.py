class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]

        visited = [[False]*(n) for _ in range(m)]

        def DFS(point):
            x = point[0]
            y = point[1]
            # visited[x][y] = True
            # print(visited)

            if (x == m-1) and (y == n-1):
                return 1
            res = 0
            for i in directions:
                new_x = x + i[0]
                new_y = y + i[1]
                if (
                    (new_x>=0 and new_x < m) and
                    (new_y>=0 and new_y < n)
                ):
                    if visited[new_x][new_y]:
                        continue
                    visited[new_x][new_y] = True
                    res += DFS([new_x,new_y])
                    # print(res,point,new_x,new_y)
                    visited[new_x][new_y] = False
            
            # visited[x][y] = False
            return res
        visited[0][0] = True
        return DFS([0,0])




        