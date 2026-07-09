"""
Keep a map of opening characters to the closing equivalents

every time you encounter an opening character, add it to a stack
every time you encounter a closing character, peek the top of the stack,
    if it top of stack matches the closing character, then pop, else return false

return len(stack) == 0
"""
class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for char in s:
            if char in paren_map.keys():
                stack.append(char)
            else:
                if len(stack) > 0 and paren_map[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

