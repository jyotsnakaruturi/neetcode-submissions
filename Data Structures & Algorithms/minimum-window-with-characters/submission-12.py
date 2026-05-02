class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""
        count={}
        window={}
        resl=float('inf')
        for i in t:
            count[i] =1+count.get(i,0)
        
        l=0
        need=len(count)
        have=0
        res=[-1,-1]
        for c in range (len(s)):
            window[s[c]]=1+window.get(s[c],0)
            if s[c] in count and window[s[c]] == count[s[c]]:
                have+=1
                while need == have:
                    if c-l+1 < resl:
                        res=[l,c]
                        resl=c-l+1
                    window[s[l]]-=1
                    if s[l] in count and window[s[l]] < count[s[l]]:
                        have -=1
                    l+=1
        return s[res[0]:res[1]+1] if resl != float('inf') else ""

        