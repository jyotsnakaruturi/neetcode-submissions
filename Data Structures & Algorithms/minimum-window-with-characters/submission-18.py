class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        maps = defaultdict(int)
        map_t = Counter(t)
        res =[]
        need =0
        mine =float('inf')
        for r in range (len(s)):
            maps[s[r]] +=1
            if s[r] in map_t and maps[s[r]] == map_t[s[r]]:
                need+=1
            while need == len(map_t):
                if l<len(s):
                    var = s[l]
                else:
                    break
                if mine > r-l+1 :
                    mine=r-l+1
                    res = [l,r]
                if var in map_t and maps[var] == map_t[var]:
                    need -=1
                maps[var] -=1
                l+=1
        return  s[res[0]:res[1]+1] if res else ""


        