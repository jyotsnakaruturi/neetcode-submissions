class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1={}
        for i in s1:
            mp1[i]=mp1.get(i,0)+1
        n=len(mp1)
        for i in range (len(s2)):
            mp2={}
            curr=0
            for j in range (i,len(s2)):
                mp2[s2[j]]=mp2.get(s2[j],0)+1
                if mp1.get(s2[j],0) < mp2[s2[j]]:
                    break
                if mp1.get(s2[j],0) == mp2[s2[j]]:
                    curr+=1
                if curr==n:
                    return True
        return False
             
         
        