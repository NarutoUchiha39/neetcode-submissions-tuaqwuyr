from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for i in range(n)] for j in range(n)]
        res = [ ]


        def check(board,row,col):
                

                dummyRow = row
                dummyCol = col

                while(dummyCol >= 0):
                    
                    if( board[dummyRow][dummyCol] == "Q" ):
                        return False
                    dummyCol -= 1

                dummyCol = col
                dummyRow = row

                while( dummyCol >=0 and dummyRow >= 0 ):
                   
                    if( board[dummyRow][dummyCol] == "Q" ):
                        return False
                    dummyCol -= 1
                    dummyRow -= 1

                dummyRow = row
                dummyCol = col

                while( dummyCol >=0 and dummyRow < len(board) ):
                    
                    if( board[dummyRow][dummyCol] == "Q" ):
                        return False
                    dummyCol -= 1
                    dummyRow += 1

                dummyRow = row
                dummyCol = col

                return True


        def traverse(index):
            if(index == len(board[0])):
                
                ok = []
                for i in board:
                    str1 = ""
                    for j in i:
                        str1 += j
                    ok.append(str1)
                res.append(deepcopy(ok))
                return 

            for i in range(len(board)):
                if(check(board,i,index)):
                    board[i][index] = "Q"
                    traverse(index+1)
                    board[i][index] = "."
    
        traverse(0)
        return res



        