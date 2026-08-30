class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        self.k = k
        heapq.heapify(self.heap)
        # print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        res =[]
        ele = self.heap[0]
        length = min(len(self.heap),self.k)
        # print("========>")

        for i in range(length):
            ele = heapq.heappop(self.heap)
            res.append(ele)
        
        # print(res,self.heap)
        
        for j in range(length):
            heapq.heappush(self.heap,res[j])
        
        # print(res,self.heap)
        # print("========>")

        return -ele
