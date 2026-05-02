class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        if t == s : return t
         
        l=0
        resl=float('inf')
        res=[-1,-1]
        have =0
        from collections import Counter
        countert=Counter(t)
        need=len(countert)
        counters={}
        for i in range (len(s)):
            counters[s[i]] = counters.get(s[i],0)+1
            if s[i] in countert and counters[s[i]] == countert[s[i]]:
                have += 1
            while need == have :
                if resl > i-l+1:
                    res = [l,i]
                    resl=i-l+1
                counters[s[l]] -=1
                if s[l] in countert and countert[s[l]] > counters[s[l]]:
                    have-=1
                l+=1

            
        if resl != float('inf') : 
            return s[res[0]:res[1]+1]
        else:
            return ""