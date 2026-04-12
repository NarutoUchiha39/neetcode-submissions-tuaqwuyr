class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        distance = [float("inf") for i in range(n+1)]
        visited = set()
        
        for i in times:
            graph[i[0]].append([i[1],i[2]])

        cost_ = 0

        heap = [[0,k]]
        while(len(visited) != n and heap):
            element = heapq.heappop(heap)
            cost = element[0]
            point = element[1]
            
            distance[point] = cost
            visited.add(point)
            
            cost_ += cost

            for i in graph[point]:
                if(i[0] not in visited):
                    heapq.heappush(heap,[cost+i[1],i[0]])
            

        return max(distance[1:]) if len(visited) == n else -1
            

        
