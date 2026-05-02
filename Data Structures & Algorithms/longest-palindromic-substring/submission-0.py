class Solution:
    def longestPalindrome(self, s: str) -> str:
        ind1=0
        lenind=0
        for i in range (len(s)):
            l,r=i,i
            while l >=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > lenind:
                    ind1=l
                    lenind=r-l+1
                r+=1
                l-=1
            l,r=i,i+1
            while l >=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > lenind:
                    ind1=l
                    lenind=r-l+1
                r+=1
                l-=1
        return s[ind1:ind1+lenind]

        