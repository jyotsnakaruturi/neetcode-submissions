class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        count1=Counter(s1)
        need=len(count1)
        for i in range (len(s2)):
            c,count2=0,{}
            for j in range (i,len(s2)):
                count2[s2[j]]=1+count2.get(s2[j],0)
                if  count1.get(s2[j],0)<count2.get(s2[j],0):
                    break
                if count1.get(s2[j],0)==count2.get(s2[j],0):
                    c+=1
                if need==c:
                    return True
        return False

