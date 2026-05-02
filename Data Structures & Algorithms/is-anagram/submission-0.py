class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        if len(s)!=len(t):
            return False
        for i in s:
            h1[i]=h1.get(i,0)+1
        for j in t:
            h2[j]=h2.get(j,0)+1
        for i in h1:
            if i not in h2 or h1[i]!=h2[i]:
                return False
        return True
