class Solution:
    def isValid(self, s: str) -> bool:
        map = {'{':'}','[':']','(':')'} 
        seen = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                seen.append(i)
            else:
                if not seen or i != map[seen[-1]]:
                    return False
                else:
                    seen.pop()
        if seen:
            return False
        else:
            return True