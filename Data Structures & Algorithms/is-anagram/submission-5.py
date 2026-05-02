from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S=[0]*26
        for i in range (len(s)):
            S[ord(s[i])- ord('a')]+=1
            S[ord(t[i])- ord('a')]-=1
        for i in S:
            if i!=0:
                return False
        return True

    
        