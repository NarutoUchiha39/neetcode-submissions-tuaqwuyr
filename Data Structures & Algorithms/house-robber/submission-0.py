class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_not_rob = [0,0]
        for i in range(len(nums)):
            temp = rob_not_rob[0]
            rob_not_rob[0] = nums[i] + rob_not_rob[1]
            rob_not_rob[1] = max(temp,rob_not_rob[1])

        return max(rob_not_rob)
        