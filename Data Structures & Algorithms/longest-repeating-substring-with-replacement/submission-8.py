class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        maxe=res=0
        l=0
        for i in range (len(s)):
            d[s[i]]=d.get(s[i],0)+1
            maxe=max(maxe,d[s[i]])

            while (i-l+1) - maxe > k:
                d[s[l]] -=1
                l+=1
            res=max(res,i-l+1)
        return res
        