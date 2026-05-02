class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Ss=defaultdict(int)
        St=defaultdict(int)
        for i in range(len(s)):
            Ss[s[i]]+=1
            St[t[i]]+=1
        return Ss==St
        