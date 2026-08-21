from typing import List


class TreeNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False
class Trie:
    def __init__(self):
        self.root=TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for u in word:
            if u not in cur.children:
                cur.children[u] = TreeNode()
            cur = cur.children[u]
        cur.end_of_word=True
        
    def search(self, word: str) -> TreeNode:
        cur = self.root
        for u in word:
            if(u  in cur.children):
                cur = cur.children[u]
            else:
                return False
        return cur
        

class Solution:

    def exist(self, board: List[List[str]],trie:Trie) -> str:

        globalRes = []
        done = set()

        def search(row,col,curWord):
            
            if((row < 0 or row >= len(board)) or (col <0 or col >= len(board[0]))):
                return False
            
            if(board[row][col] == "*"):
                return False

            curChar = board[row][col]
            curWord = curWord + curChar
            res = trie.search(curWord)

            if(type(res) == bool):
                return False

            if(res.end_of_word):
                if(curWord not in done):
                    globalRes.append(curWord)
                    done.add(curWord)

                # print(curWord,globalRes)
            
            board[row][col] = "*"

            res = (search(row+1,col,curWord)) or \
                            (search(row,col+1,curWord)) or \
                            (search(row,col-1,curWord)) or \
                            (search(row-1,col,curWord))

            board[row][col] = curChar
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                    ress = trie.search(board[i][j])
                    if(type(ress) != bool):
                        # print("=================>")
                        search(i,j,"")
                        # print("=================>")
                        

        return globalRes


        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie:Trie = Trie()
        for i in words:
            trie.insert(i)
        return self.exist(board,trie)
