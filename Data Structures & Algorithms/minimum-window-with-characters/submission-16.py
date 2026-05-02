class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return " "
        if t == s: return t
        count={}
        window={}
        res=[-1,-1]
        resl=float('inf')
        
        have=0
        l=0
        for i in t:
            count[i] = count.get(i,0)+1
        need=len(count)
        for r in range (len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have +=1
                while need == have:
                    if r-l+1 < resl:
                        res=[l,r]
                        resl=r-l+1
                    window[s[l]]-=1
                    
                    if s[l] in count and window[s[l]] < count[s[l]]:
                        have-=1
                    l+=1
        if resl != float('inf'):
            return(s[res[0]:res[1]+1])
        else:
            return ""
