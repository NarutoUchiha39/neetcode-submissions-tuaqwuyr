class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        list1 = []
        done = set()

        for i in nums:
            heapq.heappush(list1,-i)
        
        num = 0
        res = None

        while(num < k):
            
            res = heapq.heappop(list1)
            num+=1
        
        return -res
        