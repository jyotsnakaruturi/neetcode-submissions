class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #[10,15,20]0
        cost.append(0)
        for i in range (len(cost)-3,-1,-1): #as we can take 2 steps we will start from 15
            cost[i]=min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1]) #we can only start at index1 or 0
        