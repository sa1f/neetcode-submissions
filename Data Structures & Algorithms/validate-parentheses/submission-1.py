"""
keep a stack, whenever you encounter an opening bracket
put it in stack, when encountering open bracket see if you have a matching 
bracket at the top of the stack
    if true
        pop it, and continue
    else:
        return False

finally return True if len of stack is 0

"""

brackets = {
 '}': '{',
 ')': '(',
 ']': '['
}

def is_open(char):
    return char in brackets.values()


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if is_open(char):
                stack.append(char)
            else:
                if stack and brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
