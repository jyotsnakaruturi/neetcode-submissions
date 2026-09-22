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
            if s2[i] in maps1 and maps1[s2[i]] == map[s2[i]]:
                length +=1
            if (i-j+1) > len(s1):
                if s2[j] in maps1 and maps1[s2[j]] == map[s2[j]]:
                    length -=1
                map[s2[j]]-=1
                j+=1
            if need == length:
                return True
        return False
