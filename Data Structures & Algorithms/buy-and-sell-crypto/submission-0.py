class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0 
        right=1
        n=len(prices)
        maxe=0
        while right<n:
            if prices[left]<prices[right]:
                maxe=max(maxe,(prices[right]-prices[left]))
            else:
                left=right
            right+=1
        return maxe

            

