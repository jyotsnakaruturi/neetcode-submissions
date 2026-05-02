class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i not in "+-*/":
                l.append(int(i))
            else:
                a=l.pop()
                b=l.pop()
                if i=="+":
                    l.append(b+a)
                elif i=="-":
                    l.append(b-a)
                elif i=="*":
                    l.append(a*b)
                else:
                    l.append(int(b/a))
        return l[0]
        