class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        set1 = set(nums)
        longest = 0
        max_length = 0

        for i in range(len(nums)):
         if(nums[i]-1 not in set1 ):
            length = 0
            ok = nums[i]
            while(ok in set1):
                length += 1
                ok+=1
            max_length = max(max_length,length)

        return max_length


