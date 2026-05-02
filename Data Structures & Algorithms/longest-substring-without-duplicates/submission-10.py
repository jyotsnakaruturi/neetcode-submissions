class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=set()
        i=0
        c=0
        maxc=0
        for j in range (len(s)):
            while s[j] in l:
                l.remove(s[i])
                i+=1
            l.add(s[j])
            maxc=max(j-i+1,maxc)
        return maxc