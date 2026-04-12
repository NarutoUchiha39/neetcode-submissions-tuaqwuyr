"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashmap = defaultdict(None)
        def DFS(head):
            
            if(head == None):
                return None
            elif(head in hashmap):
                return hashmap[head]
            else:
                new_node = Node(head.val)
                hashmap[head] = new_node
                new_node.next = DFS(head.next)
                new_node.random = DFS(head.random)
                return new_node    
            
            
        return DFS(head)