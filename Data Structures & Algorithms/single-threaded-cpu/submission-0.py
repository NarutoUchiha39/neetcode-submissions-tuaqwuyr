class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort(key=lambda x: x[0])
        final_res = []
        minHeap = []
        i = 0
        t = 0

        while(i<len(tasks) or minHeap):
            
            # print(minHeap,i,t,tasks[i][0])
            while(i<len(tasks) and t >= tasks[i][0]):
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i+=1

            if(minHeap):
                res = heapq.heappop(minHeap)
                final_res.append(res[1])
                t += res[0]
            else:
                # print(minHeap)
                t = tasks[i][0]
            
            

        return final_res
