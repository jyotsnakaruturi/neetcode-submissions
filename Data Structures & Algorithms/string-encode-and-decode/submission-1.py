class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range (len(strs)):
            s+=strs[i]
            s+="🤣"
             
        return s

    def decode(self, s: str) -> List[str]:
        encode_l=[]
        st=""
        for i in s:
            if i!="🤣":
                st+=i
            else:
                encode_l.append(st)
                st=""
        return encode_l
