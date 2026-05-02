class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        L=[]
        
        for i in range (k,len(nums)+1):
            maxe=float('-inf')
            for j in range(l,i):
                maxe=max(maxe,nums[j])
            L.append(maxe)
            l+=1
        return L


        