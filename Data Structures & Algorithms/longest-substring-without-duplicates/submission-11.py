class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=set()
        i=0
        max_len=0
        for j,val in enumerate (s):
            while val in l:
                l.remove(s[i])
                i+=1
            l.add(val)
            max_len=max(max_len,j-i+1)
        return max_len