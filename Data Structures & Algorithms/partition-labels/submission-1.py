class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i,v in enumerate(s):
            lastindex[v]=i
        size=end=0
        res=[]
        for i,c in enumerate(s):
            size+=1
            end=max(end,lastindex[c])
            if i==end:
                res.append(size)
                size=0
        return res
                
        