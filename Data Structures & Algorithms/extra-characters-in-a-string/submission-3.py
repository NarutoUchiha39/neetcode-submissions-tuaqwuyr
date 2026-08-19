from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word_end = False

class Trie:

    def __init__(self) -> None:
        self.root = Node()
    
    def addWord(self,word):
        Node1 = self.root
        for i in word:
            if(i not in Node1.children):
                Node1.children[i] = Node()
            Node1 = Node1.children[i]
        Node1.is_word_end = True

    def Search(self,word):
        Node = self.root
        for i in word:
            if(i in Node.children):
                Node = Node.children[i]
            else:
                return False
        return True and Node.is_word_end


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        trie = Trie()
        for i in dictionary:
            trie.addWord(i)

        DP = {}

        def DFS(index):
            if(index == len(s)):
                return 0
            if(index in DP):
                return DP[index]

            res = 1+DFS(index+1)
            for i in range(index,len(s)):
                if(trie.Search(s[index:i+1])):
                    res = min(res,DFS(i+1))
            
            DP[index] = res
            return res
        
        return DFS(0)

        