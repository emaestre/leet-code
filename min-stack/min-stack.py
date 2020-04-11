class MinStack:
    def __init__(self):
        """
        Every element in the stack is a tuple with the form (value, minValue), 
        tha top value of the stack will have the minValue.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x,x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
