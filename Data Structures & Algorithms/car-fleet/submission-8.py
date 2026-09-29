class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        for i in range (len(speed)):
            ps.append([position[i],speed[i]])
        ps.sort(reverse=True)
        stack = []
        for i in ps:
            time = (target - i[0])/i[1]
            stack.append(time)
            if len(stack) >= 2 and   stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)

        