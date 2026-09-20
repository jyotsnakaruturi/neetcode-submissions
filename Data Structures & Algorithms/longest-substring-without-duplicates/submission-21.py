class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        l=0
        max_len =0
        for i in range (len(s)):
            while s[i] in map:
                map.remove(s[l])
                l+=1
            map.add(s[i])
            max_len = max(max_len,i-l+1)
        return max_len

        