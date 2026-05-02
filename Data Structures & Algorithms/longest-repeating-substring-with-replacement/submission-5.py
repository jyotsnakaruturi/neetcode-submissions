class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        maxm=0
        res=0
        l=0
        for r,i in enumerate(s):
            d[i]=1+d.get(i,0)
            maxm=max(maxm,d[i])

            while (r-l+1)-maxm >k:
                d[s[l]] -=1
                l+=1
            res=max(res,r-l+1)
        return res



        