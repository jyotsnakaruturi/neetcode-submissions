class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        k=len(s1)
        s1c = Counter(s1)
        s2c = defaultdict(int)
        for r in range (len(s2)):
            s2c[s2[r]]  +=1
            if r-l == k-1:
                s2c = Counter(s2[l:r+1])
                if s2c == s1c:
                    return True
                del s2c[s2[l]]
                l+=1
        return False

            
            

        