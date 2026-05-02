class Solution:
    def reverse(self, x: int) -> int:
        org=x
        x=abs(x)
        r=str(x)
        r=int(r[::-1])
        if org<0:
            r=r*(-1)
        if r< -(pow(2,31)) or r>(pow(2,31)-1):
            return 0
        return r