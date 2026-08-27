class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        if(self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]):
            ele = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-ele)

        if(len(self.maxHeap) - len(self.minHeap) >1):
            ele = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-ele)

        elif(len(self.minHeap) - len(self.maxHeap) >1):
            ele = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-ele)

    def findMedian(self) -> float:
        tot = len(self.maxHeap) + len(self.minHeap)
        if(tot%2):
            if(len(self.maxHeap)>len(self.minHeap)):
                return -self.maxHeap[0]
            else:
                return(self.minHeap[0])
        else:
            return(-self.maxHeap[0]+self.minHeap[0])/2
        
        