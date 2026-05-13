class Solution:
    def isValid(self, s: str) -> bool:
        map={"}":"{","]":"[",")":"("}
        stack = []
        if len(s) <2:
            return False
        for i in s:
            if i == "[" or i == "{" or i =="(":
                stack.append(i)
            else:
                if not stack or map[i] != stack.pop():
                    return False
                 

        if stack :
            return False
        else:
            return True
                
        