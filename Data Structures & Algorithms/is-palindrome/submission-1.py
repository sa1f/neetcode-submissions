"""
s -> max length, min length, alphabet?

ideas:

have a left and right pointer

while l < r:
    if s[l] != s[r]
      return false

return true

o(n/2)
o(1) space

s = "Was it a car or a cat I saw?"

l = 0
r = 28


"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            l_char = s[l]
            r_char = s[r]

            if not l_char.isalnum():
                l += 1
                continue
            if not r_char.isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True
        