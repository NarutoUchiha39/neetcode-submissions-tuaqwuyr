"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def DFS(n,r,c):

            Same = True
            for i in range(n):
                for j in range(n):
                    if(grid[r][c] != grid[r+i][c+j]):
                        Same = False
                        break
            
            if Same:
                return Node(grid[r][c],True)
            
            n = n//2
            topLeft = DFS(n,r,c)
            topRight = DFS(n,r,c+n)
            bottomLeft = DFS(n,r+n,c)
            bottomRight = DFS(n,r+n,c+n)
            
            return Node(True,False,topLeft,topRight,bottomLeft,bottomRight)
        
        return DFS(len(grid),0,0)

