class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in digits:
             
            res=res*10+i
        res=res+1

        l=[]
        while res:
            r=res%10
            l.append(r)
            res=res//10
        l.reverse()
        return l
