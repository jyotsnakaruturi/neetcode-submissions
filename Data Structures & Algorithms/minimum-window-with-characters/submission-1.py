class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1={}
        for i in t:
            mp1[i]=mp1.get(i,0)+1
        need=len(mp1)
        maxe=0
        mp={}
        reslen=float("inf")
        res=[-1,-1]
        for i in range (len(s)):
            mp2={}
            count=0
            for j in range (i,len(s)):
                mp2[s[j]]=mp2.get(s[j],0)+1
                flag=True
                for c in mp1:
                    if mp1[c]>mp2.get(c,0):
                        flag=False
                        break
                if flag and (j-i+1)<reslen:
                    reslen=j-i+1
                    res=[i,j]
        return s[res[0]:res[1]+1] if reslen!=float("inf") else ""
        