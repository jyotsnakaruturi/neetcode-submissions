class Solution:
    def isValid(self, s: str) -> bool:
       map = {'}':'{',']':'[',')':'('} 
       seen = []
       for i in s:
        if i == '{' or i == '(' or i == '[':
            seen.append(i)
        else:
            if  seen and i != map[seen[-1]]:
                return False
        return True