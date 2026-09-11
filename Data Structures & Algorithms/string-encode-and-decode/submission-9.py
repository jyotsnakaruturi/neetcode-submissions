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
            while s[i] != '#':
                i += 1
            n = int(s[j:i])
            j = i+1
            res.append(s[j:j+n])
            i = j+n
        return res

             
            


