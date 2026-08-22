from typing import List
import heapq
import math

class Solution:
    def getDistanceFromOrigin(self,x,y)->float:
        return  math.sqrt((0-x)**2+(0-y)**2)
     
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list1:List = []
        res:List = []

        for i in points:
            dist:float = self.getDistanceFromOrigin(i[0],i[1])
            # print(dist,i[0],i[1])
            heapq.heappush(list1,(dist,i[0],i[1]))

        for i in range(k):
            ele = heapq.heappop(list1)
            # print(ele[0],ele[1],ele[2])
            res.append([ele[1],ele[2]])

        return res
