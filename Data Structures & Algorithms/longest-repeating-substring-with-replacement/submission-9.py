class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map={}
        j=0
        maxe =0
        maxlen =0
        for i in range (len(s)):
            map[s[i]] = map.get(s[i],0)+1
            maxe = max(maxe,map[s[i]]) 
            while ((i-j+1)-maxe) > k:
                map[s[j]]-=1
                j+=1
            maxlen = max(maxlen,i-j+1)
        return maxlen



        