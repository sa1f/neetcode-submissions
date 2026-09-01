"""
every time you encounter an operand, open parens?

(((1+2) * 3) - 4)

operations = [(1,2,+)]
prev = (1,2,+)
curr = (prev*3)

iterate through each token
    curr      
"""


class Solution:
    def eval(self, first, second, operation):
        if operation == "+":
            return first + second
        elif operation == "-":
            return first - second
        elif operation == "*":
            return first * second
        elif operation == "/":
            return int(first / second)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for idx in range(len(tokens)):
            token = tokens[idx]
            if token not in ops:
                stack.append(token)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(self.eval(first, second, token))
        return int(stack[0])