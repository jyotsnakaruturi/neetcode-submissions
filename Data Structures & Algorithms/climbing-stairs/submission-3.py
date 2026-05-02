class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        c=0
        for i in range (n-1):
            c=a
            a=a+b
            b=c
        return a