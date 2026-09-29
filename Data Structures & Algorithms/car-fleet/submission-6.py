class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        for i in range (len(speed)):
            ps.append([position[i],speed[i]])
        ps.sort(reverse=True)
        stack = []
        for i in ps:
            time = (target - i[0])/i[1]
            while stack and time <= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)

        