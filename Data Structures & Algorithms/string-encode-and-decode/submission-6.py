class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            n=len(i)
            s+=str(n)+'#'+i
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        l=[]
        while i<len(s):
            j=i
            while j < len(s) and s[j] !="#":
                j+=1
            length=int(s[i:j])
            l.append(s[j+1:j+1+length])
            i=j+1+length
        return l


