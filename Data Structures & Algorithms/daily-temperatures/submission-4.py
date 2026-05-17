class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=0
        n=len(temperatures)
        res=[0]*(n)
        for r in range (len(temperatures)):
            maxe =temperatures[r]
            l=r+1
            while l<n-1:
                if(maxe < temperatures[l]):
                    maxe = temperatures[l]
                    res[r] = l-r
                    break
                l+=1
            
        return res

        