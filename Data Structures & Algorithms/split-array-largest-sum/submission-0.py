class Solution:

    def getGroupNums(self,nums,k,mid):
        curSum = 0
        sub = 0

        for i in nums:
            curSum+=i
            if(curSum>mid):
                curSum = i
                sub += 1
        
        return sub+1 <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        max_sum = sum(nums)
        min_sum = max(nums)

        while min_sum <= max_sum:
            mid = (max_sum + min_sum)//2
            if(self.getGroupNums(nums,k,mid)):
                max_sum = mid-1
            else:
                min_sum = mid +1
        return min_sum     
            
