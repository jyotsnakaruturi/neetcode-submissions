class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res += str(len(i))+"#"+i
        return res
         

    def decode(self, s: str) -> List[str]:
        i,j=0,0
        l=[]
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            i=j+1
            j=length+i
            word=s[i:j]
            l.append(word)
            i=j
        return l
        

