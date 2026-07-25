"""
stack1: 1, 2, 
stack: 1, 1,
"""
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()

        return self.main_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
