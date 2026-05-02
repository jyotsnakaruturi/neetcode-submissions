class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=set()
        p1=0
        c=0
        C=0
        for i in range (len(s)):
            while s[i] in l:
                c-=1
                l.remove(s[p1])
                p1+=1
            l.add(s[i])
            c+=1
            C=max(C,c)
        return C