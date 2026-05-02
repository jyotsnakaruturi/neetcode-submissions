class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mine=float('inf')
        m=float('-inf')
        for i in prices:
            mine=min(mine,i)
            m=max(m,i-mine)
        return m
        