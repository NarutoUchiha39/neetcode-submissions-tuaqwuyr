from functools import cache

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        @cache
        def DFS(left_ptr,right_ptr):
            # print(tries,left_ptr,right_ptr)
            tries = left_ptr + (len(cardPoints) - 1 - right_ptr)
            if tries >= k:
                return 0

            left = cardPoints[left_ptr]+DFS(left_ptr+1,right_ptr)
            right = cardPoints[right_ptr]+DFS(left_ptr,right_ptr-1)
            return max(left,right)
        return DFS(0,len(cardPoints)-1)


        