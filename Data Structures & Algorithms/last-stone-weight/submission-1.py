class Solution:
    def lastStoneWeight(self, stone: List[int]) -> int:
        stones = []
        for i in stone:
            stones.append(-i)
        heapq.heapify(stones)
        while len(stones) > 1:
            ele1 = heapq.heappop(stones)
            ele2 = heapq.heappop(stones)
            if(ele1 == ele2):
                heapq.heappush(stones,0)
            else:
                diff = abs(ele1-ele2)
                heapq.heappush(stones,diff if diff <0 else -diff)

            # print(stones)
        return -stones[0]