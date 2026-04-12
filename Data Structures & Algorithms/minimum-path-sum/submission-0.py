class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        grid_temp =  [[0]*(columns) for _ in range(len(grid))]
        sum_rows = 0
        sum_columns = 0

        for i in range(rows):
            sum_rows+=grid[i][0]
            # print(sum_rows)
            grid_temp[i][0] = sum_rows
        
        for i in range(columns):
            sum_columns+=grid[0][i]
            grid_temp[0][i] = sum_columns
        # print(grid_temp)
        for i in range(1,rows):
            for j in range(1,columns):
                grid_temp[i][j] = grid[i][j]+min(grid_temp[i-1][j],grid_temp[i][j-1])
        
        return grid_temp[-1][-1]


        