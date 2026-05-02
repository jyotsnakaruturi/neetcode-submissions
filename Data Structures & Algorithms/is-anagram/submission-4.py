from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S=Counter(s)
        for i in t:
            if i in S and S[i]!=0:
                S[i]-=1
            else:
                return False
        return True
    
        