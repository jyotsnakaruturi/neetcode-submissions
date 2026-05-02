from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            s.sort()
            t.sort()
        ss=Counter(s)
        tt=Counter(t)
        return tt == ss


    
        