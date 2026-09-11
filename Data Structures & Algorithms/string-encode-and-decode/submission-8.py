class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s=[]
        for i in strs:
            s.append(str(len(i)))
            s.append('#')
            s.append(i)
        return "".join(s)


    def decode(self, s: str) -> List[str]:
        res=[]

        if not s:
            return res
        i=0
        while i < len(s):
            j=i
            if s[i] != '#':
                i += 1
            n = int(s[j:i])
            j = i+1
            res.append(s[j:i+n+1])
            i = i+n+1
        return res

             
            


