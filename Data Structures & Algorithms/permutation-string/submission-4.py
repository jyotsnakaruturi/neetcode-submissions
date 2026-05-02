class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        
        s1map={}
        window_map={}
        for i in range (len(s1)):
            s1map[s1[i]]=1+s1map.get(s1[i],0)
            window_map[s2[i]]=1+window_map.get(s2[i],0)
        if s1map==window_map:
            return True
        for i in range (len(s1),len(s2)):
            end_p=s2[i-len(s1)]
            add_p=s2[i]
            window_map[add_p]=1+window_map.get(add_p,0)
            window_map[end_p]-=1
            if window_map[end_p]==0:
                del window_map[end_p]
            if window_map==s1map:
                return True
        return False

                
            
        