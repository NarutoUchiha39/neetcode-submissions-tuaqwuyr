class Node:
    def __init__(self):
        self.is_word_end = False
        self.children = {}

class PrefixTree:
         

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        Node1 = self.root
        for i in word:
            if i not in Node1.children:
                Node1.children[i] = Node()
            Node1 = Node1.children[i]
        Node1.is_word_end = True

    def search(self, word: str) -> bool:
        Node1 = self.root
        for i in word:
            if (i not in Node1.children):
                return False
            if(i in Node1.children):
                Node1 = Node1.children[i]
        return True and Node1.is_word_end

    def startsWith(self, word: str) -> bool:
        Node1 = self.root
        for i in word:
            if (i not in Node1.children):
                return False
            if(i in Node1.children):
                Node1 = Node1.children[i]
        return True
        
        
        