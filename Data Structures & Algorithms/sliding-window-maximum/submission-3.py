class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        right = 0
        left = 0
        max1 = float("-inf")
        max_index = 0
        res  =[]

        while(right - left + 1 <= k):
                    if(nums[right] > max1):
                        max1 = nums[right]
                        max_index = right
                    right += 1
        
        res.append(max1)
        left+=1

        while(right < len(nums)):

                if( max_index > left  ):
                    if(nums[right] > max1):
                        max1 = nums[right]
                        max_index = right
                    res.append(max1)
                else:
                    max1 = max(nums[left:right+1])
                    max_index = nums[left:right+1].index(max1)
                    res.append(max1)
                left+=1
                right+=1
            
        return res



