class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minStepCost = [0 for i in range(len(cost)+1)]
        for i in range (2,len(cost)+1):
            minStepCost[i] = min(minStepCost[i-1]+cost[i-1],minStepCost[i-2]+cost[i-2])
        
        return minStepCost[len(cost)]