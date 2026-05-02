class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token=[]
        for i in tokens:
            if i == "+":
                a=int(token.pop())
                b=int(token.pop())
                token.append(a+b)
            elif i == "-":
                a=int(token.pop())
                b=int(token.pop())
                token.append(b-a)
            elif i == "*":
                a=int(token.pop())
                b=int(token.pop())
                token.append(a*b)
            elif i == "/":
                a=int(token.pop())
                b=int(token.pop())
                token.append(int(b/a))
            else:
                token.append(int(i))
        return token[0]
             

        