class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = {"a":a,"b":b,"c":c}
        real_maxHeap = []
        for i in maxHeap:
            if(maxHeap[i]):
                heapq.heappush(real_maxHeap,[-maxHeap[i],i])
                
        res = ""
        while real_maxHeap:
            print(real_maxHeap,res)
            ele = heapq.heappop(real_maxHeap)
            if len(res)>=2 and res[-1] == res[-2] == ele[-1]:
                if not real_maxHeap:
                    return res
                
                second = heapq.heappop(real_maxHeap)
                counter_second = second[0]+1
                res+=second[1]
                if(counter_second):
                    heapq.heappush(real_maxHeap,[counter_second,second[1]])
                
                print(real_maxHeap)
            
            else:
                res+=ele[1]
                cnt = ele[0]+1
                
            if cnt:
                    heapq.heappush(real_maxHeap,[cnt,ele[1]])
        
        return res


