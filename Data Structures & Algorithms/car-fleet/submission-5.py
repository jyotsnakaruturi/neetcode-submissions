class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        maps=[]
        for i in range (n):
            maps.append([position[i],speed[i]])
        maps.sort(reverse = True)
        stack=[]
        for i in maps:
            stack.append((target-i[0])/i[1])
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        