import heapq
from collections import Counter,deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        MaxHeap = []
        queue = deque()
        time = 0
        Count = Counter(tasks)

        for i in Count.values():
            MaxHeap.append(-i)

        heapq.heapify(MaxHeap)

        while(MaxHeap or queue):
            time += 1

            if(MaxHeap):
                ele = 1+heapq.heappop(MaxHeap)
                if(ele):
                    queue.append([ele,time+n])
            
            if (queue and time == queue[0][1]):
                removed = queue.popleft()
                heapq.heappush(MaxHeap,removed[0])
        
        return time

