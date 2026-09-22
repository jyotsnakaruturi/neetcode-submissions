class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps1={}  
        for i in s1:
            maps1[i] = maps1.get(i,0)+1
        need = len(maps1)
        j=0
        map={}
        length =0
        for i in range (len(s2)):
            map[s2[i]] = map.get(s2[i],0)+1
            if (maps1.get(s2[i],0) < map[s2[i]]):
                map[s2[i]]-=1
                if s2[i] in maps1:
                    length -=1
                j+=1
            elif (maps1.get(s2[i],0) == map[s2[i]]):
                length+=1
            if length == need and (i-j+1) == len(s1):
                return True
        return False
            


