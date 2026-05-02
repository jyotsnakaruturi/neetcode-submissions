class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpay=prices[0]
        maxe=0
        for i in prices:
            maxe=max(maxe,i-minpay)
            minpay=min(minpay,i)
        return maxe
        