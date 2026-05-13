class Solution:
    def isValid(self, s: str) -> bool:
        map={"}":"{","]":"[",")":"("}
        stack = []
        for i in s:
            if i == "[" or i == "{" or i =="(":
                stack.append(i)
            else:
                if stack and map[i] != stack.pop():
                    return False
        if stack :
            return False
        else:
            return True
                
        