class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check9x9(i,j):
            if((i+1)%3==0 and (j + 1)%3 == 0):
                    init = j - 2
                    i = i - 2

                    row_max = i + 2
                    col_max = init + 2
                    hashmap_grid = defaultdict(int)


                    while(i <= row_max ):
                        j = init
                        while(j <= col_max):
                            if(board[i][j] in hashmap_grid):
                                return False
                            if(board[i][j] != "."):
                                hashmap_grid[board[i][j]] += 1
                            j+=1
                        i+=1
                    return True
            else:
                return True

        for i in range(len(board)):
            hashmap = defaultdict(int)
            hashmap_col = defaultdict(int)
            total_hash = defaultdict(int)

            for j in range(len(board[i])):

                if(board[j][i] in hashmap_col):
                    return False
                
                if(board[i][j] in hashmap):
                    return False
                    
                if(board[i][j]!="."):
                    hashmap[board[i][j]] += 1
                
                if(board[j][i]!="."):
                    hashmap_col[board[j][i]] += 1

                if(not check9x9(i,j)):
                    return False

        return True

                
        