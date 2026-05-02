class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""
        window={}
        count={}
        resl=float('inf')
        res=[-1,-1]

        for i in t:
            count[i]=1+count.get(i,0)

        have=0
        need=len(count)
        l=0

        for i in range (len(s)):
            c=s[i]
            window[c]=1+window.get(c,0)

            if c in count and window[c]==count[c]:
                have+=1

            while need==have:
                if (i - l + 1) < resl:
                    res = [l, i]
                    resl = i - l + 1

                window[s[l]]-=1
                if s[l] in count and window[s[l]]< count[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1]  if resl != float('inf') else ""

        




        

        