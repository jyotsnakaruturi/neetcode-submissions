class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j=0
        seen = set()
        maxlen =0
        for i in range (len(s)):
            while s[i] in seen :
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            maxlen = max(maxlen,i-j+1)
        return maxlen


        