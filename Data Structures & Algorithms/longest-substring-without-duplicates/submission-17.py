class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=set()
        l=0
        maxe=0
        max_len=0
        for r in range (len(s)):
            while s[r] in  ss:
                ss.remove(s[l])
                l+=1
                maxe-= 1
            ss.add(s[r])
            maxe+=1
            max_len=max(max_len,maxe)
        return max_len
        