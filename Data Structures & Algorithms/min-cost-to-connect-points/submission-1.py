class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        heap = [[0,points[0][0],points[0][1]]]

        def primsAlgo():

            cost = 0
            while(heap):
                popped_element = heapq.heappop(heap)
                cost_ = popped_element[0]
                x = popped_element[1]
                y = popped_element[2]

                if((x,y) not in visited):
                    cost += cost_
                    visited.add((x,y))
                    for i in points:
                        if(tuple(i) not in visited):
                            cur_cost = abs(x-i[0]) + abs(y-i[1])

                            heapq.heappush(heap,[cur_cost,i[0],i[1]])

            return cost

        
        return primsAlgo()




                




        