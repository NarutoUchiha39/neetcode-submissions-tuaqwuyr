class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles_sum = sum(piles)
        # even = True if len(piles)%2 == 0 else false
        Target = (piles_sum//2)+1
        # Tries = len(piles)//2 if even else (len(piles)//2)+1

        def DFS(i,curSum):
            if curSum >= Target:
                return True
            # if cur_try >= Tries:
            if i>=len(piles)-1:
                return False
            
            return DFS(i+2,curSum+piles[i]) or DFS(i+2,curSum+piles[len(piles)-i-1])
            
        return DFS(0,0)

        