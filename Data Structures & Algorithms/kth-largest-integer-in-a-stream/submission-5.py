class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for i in nums:
            heapq.heappush(self.heap,i)
            if(len(self.heap)>k):
                heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if (not self.heap) or len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif(val > self.heap[0]):
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)

        return self.heap[0]