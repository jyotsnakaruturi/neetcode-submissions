class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        for i in s:
            if i=="{" or i=="[" or i=="(":
                d.append(i)
            elif d and (( i=="}" and d[-1]=="{")or
                    (i=="]" and d[-1]=="[") or 
                    (i==")" and d[-1]=="(")):
                d.pop()
            else:
                return False
        if d:
            return False
        else:
            return True
        