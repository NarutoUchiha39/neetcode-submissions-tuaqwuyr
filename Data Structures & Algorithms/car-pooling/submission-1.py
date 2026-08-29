import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        curDist = 0
        curCap = 0

        for i in trips:
            heapq.heappush(minHeap,[i[1],i[2],i[0]])
        distHeap = []

        while minHeap or distHeap:
            curDist+=1
            # print(minHeap,distHeap)
            while(minHeap and minHeap[0][0]<=curDist):
                ele = heapq.heappop(minHeap)
                curCap+=ele[-1]
                heapq.heappush(distHeap,[ele[1],ele[0],ele[2]])
            
            while(distHeap and distHeap[0][0] == curDist):
                ele = heapq.heappop(distHeap)
                curCap-=ele[-1]

            if(curCap>capacity):
                    return False

        return True
