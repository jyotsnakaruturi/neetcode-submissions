class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        j=0
        S=""
        need =0
        mine = float('inf')
        mapt ={}
        for i in t:
            mapt[i] = mapt.get(i,0)+1
        n= len(mapt)
        maps={}
        for i in range (len(s)):
            maps[s[i]] = maps.get(s[i],0)+1
            if s[i] in mapt and maps[s[i]] == mapt[s[i]]:
                need +=1
            while n == need:
                if mine > (i-j+1) and need == n:
                    S=s[j:i+1]
                    mine = i-j+1
                if s[j] in mapt and maps[s[j]] == mapt[s[j]]:
                    need-=1
                maps[s[j]]-=1
                j+=1
                
            if mine > (i-j+1) and need == n:
                    S=s[j:i+1]
                    mine = i-j+1
        return S
