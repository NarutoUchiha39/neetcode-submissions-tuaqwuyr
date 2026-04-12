class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = defaultdict(int)

        def DFS(point):
            global maxi
            x = point[0]
            y = point[1]
            if (x >= ROWS or y >= COLS):
                return 0
            if((x,y) in cache):
                return cache[(x,y)]
            right = DFS((x,y+1))
            down = DFS((x+1,y))
            diag = DFS((x+1,y+1))

            if matrix[x][y] == "1":
                # print(1+min(right,down,diag))
                cache[(x,y)] = 1+min(right,down,diag)
                return cache[(x,y)]
            else:
                cache[(x,y)] = 0
                return 0

        DFS((0,0))
        return max(cache.values())**2