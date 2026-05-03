class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            n=len(i)
            s+='#'+str(n)+i
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        j=0
        for i in range (len(s)):
            if s[i] == '#':
                n=int(s[i+1])
                j=n+i
                l.append(s[i+2:j+1+1])
        return l


