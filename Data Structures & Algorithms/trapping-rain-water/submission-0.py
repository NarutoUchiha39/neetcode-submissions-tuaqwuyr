class Solution:
    def trap(self, height: List[int]) -> int:

        left,right = 0,len(height)-1
        leftMax,rightMax = height[0],height[right]
        res = 0

        while(left < right):
            if(leftMax > rightMax):
                right-=1
                rightMax = max(rightMax,height[right])
                res += rightMax - height[right]
            else:
                left+=1
                leftMax = max(leftMax,height[left])
                res += leftMax - height[left]
        return res
                
            
            

        