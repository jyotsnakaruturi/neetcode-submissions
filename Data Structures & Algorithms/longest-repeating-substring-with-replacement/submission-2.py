class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf=0
        res=0
        l=0
        mp={}
        for r in range (len(s)):
            mp[s[r]]=mp.get(s[r],0)+1
            maxf=max(maxf,mp[s[r]])
            while (r-l+1)-maxf > k:
                mp[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
        return res
            
        