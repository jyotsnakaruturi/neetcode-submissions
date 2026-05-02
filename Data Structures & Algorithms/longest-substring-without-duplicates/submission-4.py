class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        l=0
        
        maxe=0
        for  r in range (len(s)):
            while  s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            maxe=max(maxe,r-l+1)
        return maxe