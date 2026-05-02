class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        maxe=res=0
        for r,i in enumerate (s):
            d[i]=1+d.get(i,0)
            maxe=max(maxe,d[i])

            while (r-l+1) - maxe >k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res



        