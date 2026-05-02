class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ss={"}":"{","]":"[",")":"("}
        for i in s:
            if i in ss.values():
                stack.append(i)
            elif i in ss:
                if not stack or ss[i]!=stack[-1]:
                    return False
                stack.pop()    
                
        return not stack