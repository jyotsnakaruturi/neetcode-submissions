class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Ss={}
        St={}
        for i in range(len(s)):
            Ss[s[i]]=1+Ss.get(s[i],0)
            St[t[i]]=1+St.get(t[i],0)
        return Ss == St
        