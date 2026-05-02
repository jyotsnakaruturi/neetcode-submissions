class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1={}
        for i in t:
            mp1[i]=mp1.get(i,0)+1
        need=len(mp1)
        mp2={}
        have=0
        reslen=float("inf")
        res=[-1,-1]
        l=0
        for r in range (len(s)):
            mp2[s[r]]=mp2.get(s[r],0)+1
            if s[r] in mp1 and mp1[s[r]]==mp2[s[r]]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    reslen=r-l+1
                    res=[l,r]
                mp2[s[l]]-=1
                if s[l] in mp1 and mp2[s[l]]<mp1[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l : r + 1] if reslen != float("infinity") else ""    