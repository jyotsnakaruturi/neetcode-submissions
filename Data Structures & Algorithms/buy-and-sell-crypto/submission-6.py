class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxe =0
        mine= prices[0]
        for i in prices:
            mine = min(mine,i)
            maxe = max(maxe,i-mine)
        return maxe
        