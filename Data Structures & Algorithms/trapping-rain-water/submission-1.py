class Solution:
    def trap(self, height: List[int]) -> int:
        prefixarray=[0]*len(height)
        suffixarray=[0]*len(height)
        prefixarray[0]=height[0]
        n=len(height)
        for i in range (1,len(height)):
            prefixarray[i]=max(height[i],prefixarray[i-1])
        suffixarray[n-1]=height[len(height)-1]
        for i in range (len(height)-2,-1,-1):
            suffixarray[i]=max(height[i],suffixarray[i+1])
        res=0
        for i in range (len(height)):
            res+=(min(suffixarray[i],prefixarray[i]))-height[i]
        return res
        