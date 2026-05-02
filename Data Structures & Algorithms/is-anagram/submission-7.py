from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S={}
        T={}
        for i in s:
            S[i] = 1+S.get(i,0)
        for i in t:
            T[i] = 1+T.get(i,0)
        for i in S:
            if i not in T or S[i] != T[i] :
                return False
        return True


    
        