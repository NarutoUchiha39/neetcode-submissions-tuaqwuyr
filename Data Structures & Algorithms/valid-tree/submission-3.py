class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = [False for i in range(n)]
        graph = defaultdict(list)
        count = [0]
        
        if(not edges and n==1):
            return True
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        def DFS(element,par):
            if(visited[element]):
                return False

            elif(len(graph[element])==0):
                return True

            visited[element] = True

            for i in graph[element]:
                if(i != par):
                    if not(DFS(i,element)):
                        return False
            
            visited[element] = False
            count[0]+=1
            return True

        
        if not DFS(0,-1):
            return False

        if(count[0] != n):
            return False
        return True

        



    