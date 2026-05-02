class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for i in range (len(position)):
            stack.append((position[i],speed[i]))
        stack.sort(reverse=True)
        l=[]
        for p,s in stack:
            pp=(target-p)/s
            l.append(pp)
            if len(l)>1 and l[-1]<=l[-2]:
                l.pop()
        return len(l)        
