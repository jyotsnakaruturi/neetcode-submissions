class Solution:
    def reverse(self, x: int) -> int:
        res=0
        temp=x
        x=abs(x)
        while x:
            r=x%10
            x=x//10
            res=res*10+r
        if res < pow(-2,31) or res>(pow(2,31)-1):
            return 0
        else:
            if temp <0:
                return (-res)
            else:
                return res
         