class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = float("-inf")

        while( left < right ):

            max_water = max( max_water,(right - left)*( min(heights[left],heights[right] )) )
            if( heights[left] > heights[right] ):
                right -=1

            else:
                left += 1

        return max_water

        