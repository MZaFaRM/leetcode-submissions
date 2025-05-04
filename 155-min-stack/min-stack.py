class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_history = []
        self.min_curr = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_history.append(self.min_curr)

        if val <= self.stack[self.min_curr]:
            self.min_curr = len(self.stack) - 1

    def pop(self) -> None:
        self.stack.pop()
        lost_history = self.min_history.pop()
        self.min_curr = lost_history

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack[self.min_curr]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()