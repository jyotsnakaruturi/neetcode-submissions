class MinStack:

    def __init__(self):
        self.stack =[]
        self.min_t = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_t:
            self.min_t.append(val)
        elif self.min_t[-1] >= val:
            self.min_t.append(val)
        else:
            pass

        

    def pop(self) -> None:
        a = self.stack.pop()
        if a in self.min_t:
            self.min_t.remove(a)
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.min_t[-1]
        
