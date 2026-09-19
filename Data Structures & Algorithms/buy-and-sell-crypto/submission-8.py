class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mine = float('inf')
        cost = 0
        for i in range (len(prices)):
            mine = min(mine,prices[i])
            cost = max(cost,prices[i]-mine)
        return cost
        