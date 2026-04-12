class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def DFS( board,temp,x,y ):
            

            if(len(temp) > len(word) or x <0 or y<0 or x >= len(board) or y >= len(board[0]) ):
                return False

            if(board[x][y] == "."):
                return False

            cur_word = temp + board[x][y]

            if(len(cur_word) == len(word) and cur_word == word):
                return True

            temp1 = board[x][y]
            board[x][y] = "."
            

            if( 

                DFS( board,cur_word,x-1,y ) or
                DFS( board,cur_word,x+1,y ) or
                DFS( board,cur_word,x,y+1 )or
                DFS( board,cur_word,x,y-1 )
            ):
                return True
            board[x][y] = temp1

        if(len(board[0]) == 1 and board[0][0] == word ):
            return True
        elif(len(board[0]) == 1 and board[0][0] != word ):
            return False

        
        for i in range( len(board) ):
            for j in range( len( board[0] ) ):
                    if(board[i][j] == word[0]):
                        if(DFS(board,"",i,j)):
                            return True
                    

        return False
    