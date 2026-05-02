class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ss={"}":"{",")":"(","]":"["}
        for i in s:
            if i in ss.values():
                stack.append(i)
            else:
                if  stack and stack[-1] == ss[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True