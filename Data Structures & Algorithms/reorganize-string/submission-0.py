class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        Count = Counter(s)
        for i in Count:
            maxHeap.append([-Count[i],i])
        queue = deque()
        res_str = ""
        heapq.heapify(maxHeap)
        t = 0
        n = 1

        while(maxHeap or queue):
            t+=1
            if(maxHeap):
                res = heapq.heappop(maxHeap)
                if(res_str and res_str[-1] == res[1]):
                    return ""
                res_str += res[1]
                if(res[0]+1):
                    queue.append([res[0]+1,res[1],t+n])
            
            
            if (queue and t == queue[0][-1]):
                ele = queue.popleft()
                heapq.heappush(maxHeap,[ele[0],ele[1]])
        
        return res_str

