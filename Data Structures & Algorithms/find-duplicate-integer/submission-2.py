class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = 0
        slow = 0
        while(True):
            fast = nums[nums[fast]]
            slow = nums[slow]
            print(fast,slow)
            if(fast == slow):
                break
        
        ptr1 = 0 
        ptr2 = slow

        while(ptr1 != ptr2):
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr2
            

        